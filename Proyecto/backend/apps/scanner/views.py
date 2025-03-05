import os
import numpy as np
import cv2
import tensorflow as tf
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import h5py


# Construir la ruta completa al modelo
model_path = os.path.join(settings.BASE_DIR, 'models', 'modelo_final.h5')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"No se encontró el modelo en la ruta: {model_path}")
print(f"El modelo se encontró en: {model_path}, tamaño: {os.path.getsize(model_path)} bytes")

# Cargar el modelo de forma global
model = tf.keras.models.load_model(model_path)

# Diccionario que mapea los índices de predicción a las etiquetas de material
# Diccionario que mapea los índices de predicción a las nuevas etiquetas
INDEX_MAPPING = {
    0: 'battery',
    1: 'biological',
    2: 'brown-glass',
    3: 'cardboard',
    4: 'clothes',
    5: 'green-glass',
    6: 'metal',
    7: 'paper',
    8: 'plastic',
    9: 'shoes',
    10: 'trash',
    11: 'white-glass'
}

# Diccionario que mapea cada etiqueta a un mensaje de contenedor recomendado
CLASS_TO_CONTAINER = {
    'battery': 'Depósitalo en un punto de recolección de baterías o residuos peligrosos. Nunca en la basura común ni en el reciclaje.',
    'biological': 'Desecha en un contenedor especial para residuos biológicos o sanitarios. No debe mezclarse con otros residuos.',
    'brown-glass': 'Depósitalo en el contenedor de VIDRIO (si hay uno específico) o en el reciclaje si solo hay dos opciones.',
    'cardboard': 'Si está limpio y seco, colócalo en el contenedor de PAPEL/CARTÓN o en RECICLABLES. Si está sucio, tíralo a la basura general.',
    'clothes': 'Llévalo a un punto de donación de ropa o deposítalo en el contenedor textil, si está disponible. No va en reciclaje común.',
    'green-glass': 'Colócalo en el contenedor de VIDRIO (verde si hay separación por colores) o en RECICLABLES si solo hay dos opciones.',
    'metal': 'deposítalo en el contenedor de METALES o en RECICLABLES. Si está contaminado, va a la basura general.',
    'paper': 'Si está limpio y sin grasa, deposítalo en el contenedor de PAPEL/CARTÓN o en RECICLABLES. Si está sucio, va a la basura común.',
    'plastic': 'Depósitalo en el contenedor de PLÁSTICOS, o en RECICLABLES si solo hay dos opciones. Limpia los envases antes de reciclar.',
    'shoes': 'Si están en buen estado, llévalos a un punto de donación. Si están muy dañados, tíralos en la basura general, no en reciclaje.',
    'trash': 'Desecha en la basura general o en el contenedor de NO RECICLABLES si hay separación en dos tipos.',
    'white-glass': 'Depósitalo en el contenedor de VIDRIO (blanco si hay separación por colores) o en RECICLABLES si solo hay dos opciones.'
}

class PredictImageView(APIView):
    def post(self, request, format=None):
        # Verifica que se envíe la imagen
        if 'image' not in request.FILES:
            return Response({'error': 'No se ha enviado ninguna imagen.'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        image_file = request.FILES['image']
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if image is None:
            return Response({'error': 'La imagen enviada no es válida.'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Preprocesamiento: redimensionar a 224x224 y normalizar
        image_resized = cv2.resize(image, (224, 224))
        image_normalized = image_resized.astype("float32") / 255.0
        input_image = np.expand_dims(image_normalized, axis=0)
        
        # Realizar la predicción
        preds = model.predict(input_image)
        pred_index = int(np.argmax(preds, axis=1)[0])
        # Obtener la etiqueta del material usando el diccionario de mapeo
        pred_class = INDEX_MAPPING.get(pred_index, 'desconocido')
        # Obtener el mensaje de contenedor recomendado a partir de la etiqueta
        container = CLASS_TO_CONTAINER.get(pred_class, 'Contenedor desconocido')
        
        # Devolver la respuesta en formato JSON
        return Response({
            'predicted_class': pred_class,
            'recommended_container': container
        }, status=status.HTTP_200_OK)

import os
import numpy as np
import cv2
import tensorflow as tf
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import h5py

# Verificar que el archivo del modelo se pueda abrir (opcional)
try:
    with h5py.File('models/modelo_final.h5', 'r') as f:
        print("El archivo HDF5 se abrió correctamente.")
except Exception as e:
    print("Error al abrir el archivo:", e)

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
    'battery': 'Contenedor especial para baterías (residuos peligrosos)',
    'biological': 'Contenedor de residuos biológicos',
    'brown-glass': 'Contenedor para reciclaje de vidrio marrón',
    'cardboard': 'Contenedor para reciclaje de cartón',
    'clothes': 'Contenedor para donación o reciclaje de ropa',
    'green-glass': 'Contenedor para reciclaje de vidrio verde',
    'metal': 'Contenedor para reciclaje de metales',
    'paper': 'Contenedor para reciclaje de papel',
    'plastic': 'Contenedor para reciclaje de plásticos',
    'shoes': 'Contenedor para reciclaje o donación de calzado',
    'trash': 'Contenedor de basura general',
    'white-glass': 'Contenedor para reciclaje de vidrio blanco'
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

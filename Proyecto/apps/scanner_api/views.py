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
    with h5py.File('models/modelo_materiales.h5', 'r') as f:
        print("El archivo HDF5 se abrió correctamente.")
except Exception as e:
    print("Error al abrir el archivo:", e)

# Construir la ruta completa al modelo
model_path = os.path.join(settings.BASE_DIR, 'models', 'modelo_materiales.h5')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"No se encontró el modelo en la ruta: {model_path}")
print(f"El modelo se encontró en: {model_path}, tamaño: {os.path.getsize(model_path)} bytes")

# Cargar el modelo de forma global
model = tf.keras.models.load_model(model_path)

# Diccionario que mapea los índices de predicción a las etiquetas de material
INDEX_MAPPING = {
    0: 'plastico',
    1: 'vidrio',
    2: 'papel'
}

# Diccionario que mapea las etiquetas de material a los mensajes de contenedores recomendados
CLASS_TO_CONTAINER = {
    'plastico': 'Contenedor de reciclaje de plásticos',
    'vidrio': 'Contenedor de reciclaje de vidrio',
    'papel': 'Contenedor de reciclaje de papel'
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

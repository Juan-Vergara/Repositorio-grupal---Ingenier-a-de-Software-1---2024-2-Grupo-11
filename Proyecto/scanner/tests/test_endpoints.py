from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from PIL import Image
import io

class PredictEndpointTest(APITestCase):
    def test_predict_endpoint(self):
        # Asumiendo que en urls.py el endpoint se registró con el nombre 'predict-image'
        url = reverse('predict-image')
        
        # Crear una imagen de prueba en memoria (224x224, fondo rojo)
        image = Image.new('RGB', (224, 224), color=(255, 0, 0))
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        
        # Crear un objeto SimpleUploadedFile para simular la carga de la imagen
        uploaded_image = SimpleUploadedFile(
            "test.jpg", 
            image_io.read(),
            content_type="image/jpeg"
        )
        
        data = {
            'image': uploaded_image
        }
        
        # Enviar la petición POST al endpoint usando formato multipart/form-data
        response = self.client.post(url, data, format='multipart')
        
        # Comprobar que la respuesta es 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Comprobar que la respuesta JSON contiene los campos esperados
        self.assertIn('predicted_class', response.data)
        self.assertIn('recommended_container', response.data)

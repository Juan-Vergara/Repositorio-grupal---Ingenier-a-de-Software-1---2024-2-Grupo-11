from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from PIL import Image
import io

class PredictEndpointTest(APITestCase):
    def test_predict_endpoint(self):
        url = reverse('predict-image')
        
        image = Image.new('RGB', (224, 224), color=(255, 0, 0))
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        
        uploaded_image = SimpleUploadedFile(
            "test.jpg", 
            image_io.read(),
            content_type="image/jpeg"
        )
        
        data = {
            'image': uploaded_image
        }
        
        response = self.client.post(url, data, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertIn('predicted_class', response.data)
        self.assertIn('recommended_container', response.data)

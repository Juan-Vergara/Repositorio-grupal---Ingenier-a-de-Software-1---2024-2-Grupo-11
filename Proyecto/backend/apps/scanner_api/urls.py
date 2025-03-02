from django.urls import path
from .views import PredictImageView

urlpatterns = [
    path('scan/', PredictImageView.as_view(), name='predict-image'),
]
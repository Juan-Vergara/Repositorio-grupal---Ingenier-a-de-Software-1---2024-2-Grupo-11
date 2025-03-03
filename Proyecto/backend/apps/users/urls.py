from django.urls import path
from .views import RegisterView  # Importa la vista de registro
from .views import LoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Agrega la ruta de registro
    path('login/', LoginView.as_view(), name='login'),
]

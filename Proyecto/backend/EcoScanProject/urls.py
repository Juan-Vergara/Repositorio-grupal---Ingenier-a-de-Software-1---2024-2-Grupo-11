from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.scanner.urls')),  # Importa las rutas de apps.scanner
    path('api/', include('apps.users.urls')),  # Importa las rutas de apps.users
]
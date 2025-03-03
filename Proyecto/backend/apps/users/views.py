from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.authtoken.models import Token
import logging

# Configurar logger para depuración
logger = logging.getLogger(__name__)

User = get_user_model()

def post(self, request):
    # Añade estos logs detallados al principio de tu método
    print("==== DEBUG LOGIN ====")
    print("Contenido completo de request.data:", request.data)
    print("Tipo de request.data:", type(request.data))
    print("Headers:", request.headers)
    
    # Intenta acceder a los datos de diferentes maneras
    print("request.data.get('email'):", request.data.get('email'))
    print("'email' in request.data:", 'email' in request.data)
    print("Llaves en request.data:", request.data.keys())
    
    # Si estás usando request.POST en algún lugar
    print("request.POST:", request.POST)
    
    # El resto de tu código...

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        try:
            # Registra la información recibida para depuración
            logger.info(f"Datos recibidos: {request.data}")
            
            # Obtener credenciales
            email = request.data.get('email')
            password = request.data.get('password')
            
            # Validación básica
            if not email or not password:
                logger.warning(f"Intento de login sin email o password completos")
                return Response({"error": "Email y contraseña son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Verificar si el usuario existe
            try:
                user = User.objects.get(email=email)
                logger.info(f"Usuario encontrado con email: {email}")
            except User.DoesNotExist:
                logger.warning(f"No se encontró usuario con email: {email}")
                return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Intentar autenticar usando el username del usuario encontrado
            user = authenticate(username=user.username, password=password)
            
            if user is not None:
                # Login exitoso
                login(request, user)
                
                # Crear o recuperar token
                token, created = Token.objects.get_or_create(user=user)
                logger.info(f"Login exitoso para usuario: {email}")
                
                # Devolver token de acceso
                return Response({
                    "access": token.key,
                    "user_id": user.id,
                    "email": user.email
                }, status=status.HTTP_200_OK)
            else:
                # Password incorrecto
                logger.warning(f"Password incorrecto para usuario: {email}")
                return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            # Registrar cualquier excepción no controlada
            logger.error(f"Error en login: {str(e)}")
            return Response({"error": "Error en el servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
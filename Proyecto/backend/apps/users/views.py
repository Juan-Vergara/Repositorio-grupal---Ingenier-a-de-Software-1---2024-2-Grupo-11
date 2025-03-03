from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.authtoken.models import Token
import logging
from .models import Usuario

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
        print("DATOS DE REGISTRO RECIBIDOS:", request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"USUARIO CREADO: nombre={user.nombre}, email={user.email}")
            return Response({'message': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        
        print("ERRORES DE REGISTRO:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        try:
            print("Datos recibidos:", request.data)
            
            email = request.data.get('email')
            password = request.data.get('password')
            
            if not email or not password:
                return Response({"error": "Email y contraseña son obligatorios"}, status=400)
            
            # Intenta encontrar el usuario sin generar excepción
            user = Usuario.objects.filter(email=email).first()
            
            if user and user.check_password(password):
                # Responde sin crear token primero para ver si eso funciona
                return Response({
                    "access": "token_temporal_de_prueba",
                    "user_id": user.id,
                    "email": user.email
                }, status=200)
            else:
                return Response({"error": "Credenciales inválidas"}, status=400)
                
        except Exception as e:
            # Captura cualquier excepción y registra el error completo
            import traceback
            print("ERROR COMPLETO:", str(e))
            print(traceback.format_exc())
            return Response({"error": "Error en el servidor", "details": str(e)}, status=500)
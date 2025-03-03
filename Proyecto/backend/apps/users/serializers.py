# serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario(
            email=validated_data["email"],
            nombre=validated_data["nombre"],
        )
        user.set_password(validated_data["password"])  # <--- encripta la contraseña
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()  # asumiendo login por email
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Autenticar con email (requiere un backend que acepte email como "username")
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError("Credenciales incorrectas")
        data['user'] = user
        return data

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Encripta la contraseña correctamente
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):  
        return self.get(email=email)  

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = None  

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """Asegurar que la contraseña se guarde encriptada."""
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)  # Encripta si no está encriptada
        super().save(*args, **kwargs)

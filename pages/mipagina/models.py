from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

#modelo del usario personalizado del proyecto final
class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True, max_length=1)

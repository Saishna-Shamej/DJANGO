from django.contrib.auth.models import AbstractUser
from django.db import models

from django import forms

# Create your models here.
class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
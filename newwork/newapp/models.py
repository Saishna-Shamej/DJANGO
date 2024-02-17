from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class myuser(AbstractUser):
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)

    is_guest = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

class File(models.Model):
    title = models.CharField(max_length=120)
    topic = models.CharField(max_length=60)

    pdf = models.FileField(upload_to="file/pdf")
    cover = models.ImageField(upload_to="file/cover")
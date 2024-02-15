from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class worker(AbstractUser):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

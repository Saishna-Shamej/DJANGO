from django.db import models


# Create your models here.

class product(models.Model):
    item_name = models.CharField(max_length=24)
    item_img = models.ImageField()

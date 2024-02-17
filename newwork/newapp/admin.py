from django.contrib import admin

from .models import myuser, File

# Register your models here.
admin.site.register(myuser)

admin.site.register(File)
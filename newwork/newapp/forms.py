from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import myuser, File


class myuserForm(UserCreationForm):
    class Meta:
        model = myuser
        fields = UserCreationForm.Meta.fields + ('email', 'phone')

class fileForm(forms.ModelForm):
    class Meta:
        model=File
        fields="__all__"
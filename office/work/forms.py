from django.contrib.auth.forms import UserCreationForm

from .models import worker


class workerCreationForm(UserCreationForm):
    class Meta:
        model = worker
        fields = UserCreationForm.Meta.fields + ('email', 'phone')
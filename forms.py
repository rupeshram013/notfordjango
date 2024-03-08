from django.forms import ModelForm
from .models import Register

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
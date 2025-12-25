from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

# Formulario de Registro (con Email)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email')

# Formulario para Editar Perfil
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

# Formulario para subir/cambiar Avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('imagen',)
from django import forms
from .models import *
# Estos son los traductores: convierten tu Modelo en campos HTML
class LanaForm(forms.ModelForm):
    class Meta:
        model = Lana
        fields = '__all__' # Crea inputs para todos los campos

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    # Campo especial para elegir usuario (filtro para no mandarse a sí mismo si quisieras, pero simple por ahora)
    receptor = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        label="Para", 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    cuerpo = forms.CharField(
        label="Mensaje", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    class Meta:
        model = Mensaje
        fields = ['receptor', 'cuerpo']
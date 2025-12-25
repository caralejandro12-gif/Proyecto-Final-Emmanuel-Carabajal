from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User

@login_required
def inbox(request):
    # Filtramos los mensajes donde el receptor soy YO
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, "mensajeria/inbox.html", {"mensajes": mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user # El emisor soy YO automáticamente
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    
    return render(request, "mensajeria/enviar_mensaje.html", {"form": form})
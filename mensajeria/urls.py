from django.urls import path
from .views import *

urlpatterns = [
    path("inbox/", inbox, name="inbox"),
    path("enviar/", enviar_mensaje, name="enviar_mensaje"),
]
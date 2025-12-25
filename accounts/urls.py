from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_request, register, editar_perfil

urlpatterns = [
    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('perfil/', editar_perfil, name='editar_perfil'),
]
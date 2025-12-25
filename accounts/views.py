from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm, AvatarForm
from .models import Avatar

# 1. LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    
    return render(request, "accounts/login.html", {"form": form})

# 2. REGISTRO
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creamos un avatar vacío para el usuario nuevo
            Avatar.objects.create(user=user)
            login(request, user) # Lo logueamos directo
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    
    return render(request, "accounts/register.html", {"form": form})

# 3. EDITAR PERFIL Y AVATAR
@login_required
def editar_perfil(request):
    usuario = request.user
    # Intentamos obtener el avatar, si no existe (por errores viejos) lo creamos
    avatar, created = Avatar.objects.get_or_create(user=usuario)

    if request.method == "POST":
        # Formulario de datos personales
        miFormulario = UserEditForm(request.POST, instance=usuario)
        # Formulario de Avatar (con request.FILES para la foto)
        miAvatar = AvatarForm(request.POST, request.FILES, instance=avatar)

        if miFormulario.is_valid() and miAvatar.is_valid():
            miFormulario.save()
            miAvatar.save()
            return redirect('inicio')
    else:
        miFormulario = UserEditForm(instance=usuario)
        miAvatar = AvatarForm(instance=avatar)

    return render(request, "accounts/perfil.html", {
        "form": miFormulario, 
        "avatar_form": miAvatar,
        "avatar_actual": avatar
    })
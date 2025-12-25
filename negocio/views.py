from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# --- VISTA DE INICIO ---
"""def home(request):
    # Buscamos todos los productos cargados en la base de datos
    productos = Product.objects.all()
    # Se los enviamos al template
    return render(request, "negocio/index.html", {"products": productos})"""
    
def home(request):
    productos = Product.objects.all()
    lanas = Lana.objects.all()
    herramientas = Herramienta.objects.all() 
    
    return render(request, "negocio/index.html", {
        "products": productos, 
        "lanas": lanas,
        "herramientas": herramientas})

# --- VISTAS DE FORMULARIOS ---

def crear_lana(request):
    if request.method == "POST":
        # Si el usuario llenó el form y dio Enter
        form = LanaForm(request.POST, request.FILES) # Creamos el formulario con los datos ingresados
        if form.is_valid():
            form.save() # Guardamos en la BD
            return redirect('inicio')
    else:
        
        form = LanaForm() # Creamos el formulario vacío

    return render(request, "negocio/form_lana.html", {"form": form})

def crear_herramienta(request):
    if request.method == "POST":
        form = HerramientaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = HerramientaForm()
    return render(request, "negocio/form_herramienta.html", {"form": form})

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, "negocio/form_cliente.html", {"form": form})

# --- VISTA DE BÚSQUEDA ---

def buscar_lana(request):
    marca_buscada = request.GET.get('marca') # Obtenemos lo que escribió en el input
    
    if marca_buscada:
        # Filtramos las lanas que contengan ese texto
        lanas = Lana.objects.filter(marca__icontains=marca_buscada)
    else:
        lanas = [] # Si no buscó nada, lista vacía

    return render(request, "negocio/buscar_lana.html", {"lanas": lanas})

def crear_producto(request):
    if request.method == "POST":
        # --- AGREGA ESTAS 3 LINEAS ---
        print("--------------------------------------------------")
        print("POST recibido:", request.POST)
        print("ARCHIVOS recibidos:", request.FILES) # <--- AQUÍ ESTÁ LA VERDAD
        print("--------------------------------------------------")
        # -----------------------------
        
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            # Si el formulario falla, que nos diga por qué
            print("ERRORES DEL FORMULARIO:", form.errors)
            
    else:
        form = ProductForm()
    
    return render(request, "negocio/form_producto.html", {"form": form})

# Lo nuevo para entrega final
# 1. CBV de DETALLE (Pública)
class ProductDetail(DetailView):
    model = Product
    template_name = "negocio/detalle_producto.html"
    
class LanaDetail(DetailView):
    model = Lana
    template_name = "negocio/detalle_lana.html"

class HerramientaDetail(DetailView):
    model = Herramienta
    template_name = "negocio/detalle_herramienta.html"

# 2. CBV de BORRADO (Requiere Login - Usamos Mixin)
class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "negocio/confirmar_borrado.html"
    success_url = reverse_lazy('inicio')

# 3. CBV de EDICIÓN (Requiere Login - Usamos Mixin)
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "negocio/form_producto_editar.html"
    # Estos son los campos que dejarás editar
    fields = ['nombre', 'categoria', 'subtitulo', 'descripcion', 'imagen'] 
    success_url = reverse_lazy('inicio')
    
def about(request):
    return render(request, "negocio/about.html")


class LanaUpdate(LoginRequiredMixin, UpdateView):
    model = Lana
    template_name = "negocio/form_lana_editar.html"
    fields = ['marca', 'color', 'precio', 'imagen'] 
    success_url = reverse_lazy('inicio')

class LanaDelete(LoginRequiredMixin, DeleteView):
    model = Lana
    template_name = "negocio/confirmar_borrado_lana.html"
    success_url = reverse_lazy('inicio')
    
class HerramientaUpdate(LoginRequiredMixin, UpdateView):
    model = Herramienta
    template_name = "negocio/form_herramienta_editar.html"
    fields = ['nombre', 'medida', 'imagen'] 
    success_url = reverse_lazy('inicio')

class HerramientaDelete(LoginRequiredMixin, DeleteView):
    model = Herramienta
    template_name = "negocio/confirmar_borrado_herramienta.html"
    success_url = reverse_lazy('inicio')
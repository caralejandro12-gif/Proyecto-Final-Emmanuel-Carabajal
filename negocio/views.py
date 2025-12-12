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
    
    # --- DIAGNÓSTICO ---
    print("----- LISTA DE PRODUCTOS -----")
    for p in productos:
        print(f"Producto: {p.nombre}")
        print(f"   ¿Tiene imagen?: {bool(p.imagen)}")
        print(f"   Ruta guardada: {p.imagen}")
    print("------------------------------")
    # -------------------

    lanas = Lana.objects.all() 
    return render(request, "negocio/index.html", {"products": productos, "lanas": lanas})

# --- VISTAS DE FORMULARIOS ---

def crear_lana(request):
    if request.method == "POST":
        # Si el usuario llenó el form y dio Enter
        form = LanaForm(request.POST)
        if form.is_valid():
            form.save() # Guardamos en la BD
            return redirect('inicio')
    else:
        # Si el usuario solo entró a la página
        form = LanaForm() # Creamos el formulario vacío
    
    # IMPORTANTE: Enviamos "form" al HTML para que se vean los campos
    return render(request, "negocio/form_lana.html", {"form": form})

def crear_herramienta(request):
    if request.method == "POST":
        form = HerramientaForm(request.POST)
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
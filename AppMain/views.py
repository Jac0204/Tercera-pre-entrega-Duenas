from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Categoria, Producto
from .forms import ClienteForm, CategoriaForm, ProductoForm

# Create your views here.

# Inicio
def index(request): # Se encarga de mostrar la página principal con los datos totales de cada clase/modelo
    clientes = Cliente.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'index.html', { 'clientes': clientes.__len__ , 'categorias': categorias.__len__, 'productos': productos.__len__ })

# Cliente
def cliente(request): # Se encarga de mostrar la página de Cliente con los datos de su modelo. Si es POST se realiza la inserción
    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            
            Cliente.objects.create(
                nombre_completo=info['nombre_completo'],
                fecha_nacimiento=info['fecha_nacimiento'],
                dni=info['dni'],
                email=info['email']
            )

            return redirect('cliente')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente.html', { 'form': form, 'clientes': clientes })

def buscar_cliente(request): # Se encarga de mostrar la página con la búsqueda de algún registro del modelo Cliente
    clientes = Cliente.objects.filter(nombre_completo__icontains=request.POST["nombre"])
    return render(request, 'cliente/buscar_cliente.html', { 'clientes': clientes })

# Categoría
def categoria(request): # Se encarga de mostrar la página de Categoría con los datos de su modelo. Si es POST se realiza la inserción
    if request.method == 'POST':

        form = CategoriaForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            
            Categoria.objects.create(
                nombre=info['nombre'],
                descripcion=info['descripcion']
            )

            return redirect('categoria')
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria.html', { 'form': form, 'categorias': categorias })

def buscar_categoria(request): # Se encarga de mostrar la página con la búsqueda de algún registro del modelo Categoría
    categorias = Categoria.objects.filter(nombre__icontains=request.POST["nombre"])
    return render(request, 'categoria/buscar_categoria.html', { 'categorias': categorias })

# Producto
def producto(request): # Se encarga de mostrar la página de Producto con los datos de su modelo. Si es POST se realiza la inserción
    if request.method == 'POST':

        form = ProductoForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            
            Producto.objects.create(
                nombre=info['nombre'],
                descripcion=info['descripcion'],
                categoria_id=info['categoria'],
                stock=info['stock'],
                precio=info['precio'],
                activo=info['activo']
            )

            return redirect('producto')
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, 'producto/producto.html', { 'form': form, 'productos': productos })

def buscar_producto(request): # Se encarga de mostrar la página con la búsqueda de algún registro del modelo Producto
    productos = Producto.objects.filter(nombre__icontains=request.POST["nombre"])
    return render(request, 'producto/buscar_producto.html', { 'productos': productos })

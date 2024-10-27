from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm  # Importamos el formulario que crearemos

def inicio(request):
    return render(request, 'productos/inicio.html')

def lista_productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('lista_productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})


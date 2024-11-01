from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm  
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'productos/login.html')

def inicio(request):
    return render(request, 'productos/inicio.html')

def lista_productos(request):
    productos = Producto.objects.all()  
    return render(request, 'productos/lista_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_productos')  
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

# views.py

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Opcional: inicia sesión automáticamente después del registro
            return redirect('inicio')  # Redirige a la página de inicio u otra página de tu elección
    else:
        form = CustomRegisterForm()
    return render(request, 'productos/registro.html', {'form': form})


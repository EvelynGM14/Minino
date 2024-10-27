from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
]

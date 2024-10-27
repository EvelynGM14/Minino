"""
URL configuration for minino_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # Incluimos `include` para agregar URLs de otras apps
from productos import views  # Importamos las vistas de productos

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('productos/', include('productos.urls')),  # URL para la aplicación productos
    path('', views.inicio, name='inicio'),  # Página de inicio
]


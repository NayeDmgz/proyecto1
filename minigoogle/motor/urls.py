"""
URL configuration for motor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from generales import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("formulario_busqueda/", views.mostrar_formulario_busqueda, name='formulario_busqueda'),
    path("resultados/", views.mostrar_resultados, name='mostrar_resultados'),
    # Define una vista para la URL raíz
    path("", views.mi_vista_de_inicio, name='inicio'),  # Reemplaza 'mi_vista_de_inicio' con tu vista
    path('formulario/', views.mostrar_formulario_busqueda, name='mostrar_formulario_busqueda'),
]

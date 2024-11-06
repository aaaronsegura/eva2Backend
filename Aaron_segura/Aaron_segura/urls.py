"""
URL configuration for Aaron_segura project.

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

from Aaron_seguraAPP import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_inscripciones, name='listar_inscripciones'),
    path('agregarI/', views.agregar_inscripcion, name='agregar_inscripcion'),
    path('editarI/<int:id>/', views.actualizar_inscripcion, name='actualizar_inscripcion'),
    path('eliminarI/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),

]






"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import menuprincipal, Armas, Animales, Construcciones, Consumibles, Enemigos, Flora, forowiki, inicio_sesion, Logros, Lugares, Micuenta, Recuperarcontra, Registrarse, Admin, Historia, borrarUsuario, Vcontra, ModificarC, FormularioTablas, modificarC2, penalizarUsuario, registrar_usuario,listado,ini_sesion

urlpatterns = [
    path('', menuprincipal, name='menuprincipal'),
    path('Animales/', Animales, name = 'Animales'),
    path('Armas/', Armas, name='Armas'),
    path('Construcciones/', Construcciones, name ='Construcciones'),
    path('Consumibles/', Consumibles, name='Consumibles'),
    path('Enemigos/', Enemigos, name='Enemigos'),
    path('Flora/', Flora, name='Flora'),
    path('Foro/', forowiki, name='Foro'),
    path('Inicio-sesion/', inicio_sesion, name='Inicio-sesion'),
    path('Logros/', Logros, name='Logros'),
    path('Lugares/', Lugares, name='Lugares'),
    path('Micuenta/', Micuenta, name='Micuenta'),
    path('Recuperarcontra/', Recuperarcontra, name='Recuperarcontra'),
    path('Registrarse/', Registrarse, name='Registrarse'),
    path('Admin/', listado, name='Admin'),
    path('Historia/', Historia, name='Historia'),
    path('eliminarUsuario/<id_usuario>', borrarUsuario, name="eliminarUsuario"),
    path('banearUsuario/<id_usuario>', penalizarUsuario, name="banearUsuario"),
    path('VerificarContra/', Vcontra, name='VerificarContra'),
    path('ModificarCuenta/', ModificarC, name="ModificarCuenta"),
    path('ModificarCuenta2/', modificarC2, name="ModificarCuenta2"),
    path('FormularioTablas', FormularioTablas, name='FormularioTablas'),
    path('registro/', registrar_usuario, name='registro'),
    path('listado/', listado, name='listado'),
    path('ini_sesion/', ini_sesion, name='ini_sesion'),
    

]

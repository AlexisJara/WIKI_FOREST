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
from unicodedata import name
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import registroTabla, borrarComentario, borrarContenido, listadoForo, menuprincipal, Armas, Animales, Construcciones, Consumibles, Enemigos, Flora, forowiki, inicio_sesion, Logros, Lugares, Micuenta, Recuperarcontra, Registrarse, Admin, Historia, borrarUsuario, Vcontra, ModificarC, FormularioTablas, modificarC2, penalizarUsuario, registrar_usuario,listado, ini_sesion, listadoForo, EditarTablas, modificarTabla, aniadirComentario

urlpatterns = [
    path('', menuprincipal, name='menuprincipal'),
    path('Animales/', Animales, name = 'Animales'),
    path('Armas/', Armas, name='Armas'),
    path('Construcciones/', Construcciones, name ='Construcciones'),
    path('Consumibles/', Consumibles, name='Consumibles'),
    path('Enemigos/', Enemigos, name='Enemigos'),
    path('Flora/', Flora, name='Flora'),
    path('Foro/<id_usuario>', forowiki, name='Foro'),
    path('Inicio-sesion/', inicio_sesion, name='Inicio-sesion'),
    path('Logros/', Logros, name='Logros'),
    path('Lugares/', Lugares, name='Lugares'),
    path('Micuenta/<id_usuario>', Micuenta, name='Micuenta'),
    path('Recuperarcontra/', Recuperarcontra, name='Recuperarcontra'),
    path('Registrarse/', Registrarse, name='Registrarse'),
    path('Admin/', listado, name='Admin'),
    path('Historia/', Historia, name='Historia'),
    path('eliminarContenido/<int:id_tema>', borrarContenido, name="borrarContenido"),
    path('eliminarComentario/<int:id_comentario>', borrarComentario, name="borrarComentario"),
    path('eliminarUsuario/<id_usuario>', borrarUsuario, name="eliminarUsuario"),
    path('banearUsuario/<id_usuario>', penalizarUsuario, name="banearUsuario"),
    path('VerificarContra/', Vcontra, name='VerificarContra'),
    path('ModificarCuenta/<id_usuario>', ModificarC, name="ModificarCuenta"),
    path('ModificarCuenta2/<id_usuario>', modificarC2, name="ModificarCuenta2"),
    path('FormularioTablas/', FormularioTablas, name='FormularioTablas'),
    path('EditarTablas/<int:id_tema>', EditarTablas, name='EditarTablas'),
    #Registrar datos en la tabla
    path('registroTabla/<id_usuario>', registroTabla, name = 'registroTabla'),
    #Registrar datos de un usuario
    path('registro/', registrar_usuario, name='registro'),
    path('listado/', listado, name='listado'),
    path('listadoForo/', listadoForo, name='listadoForo'),
    path('ini_sesion/', ini_sesion, name='ini_sesion'),
    path('modificarTabla/<id_usuario>', modificarTabla, name='modificarTabla'),
    path('AniadirComentario/<id>', aniadirComentario, name='aniadirComentario'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

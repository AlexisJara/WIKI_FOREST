from cgitb import html
from turtle import update
from django.shortcuts import render, redirect
from .models import TipoUsuario, Usuario,Estado
from django.contrib import messages

# Create your views here.

def menuprincipal(request):

    return render(request ,'wiki/menuprincipal.html')

def Animales(request):

    return render(request ,'wiki/Animales.html')

def Armas(request):

    return render(request ,'wiki/Armas.html')

def Construcciones(request):

    return render(request ,'wiki/Construcciones.html')

def Consumibles(request):

    return render(request ,'wiki/Consumibles.html')

    
def Enemigos(request):

    return render(request ,'wiki/Enemigos.html')

def Flora(request):

    return render(request ,'wiki/Flora.html')

def forowiki(request):

    return render(request ,'wiki/forowiki.html')

def Historia(request):

    return render(request ,'wiki/Historia.html')

def inicio_sesion(request):

    return render(request ,'wiki/inicio-sesion.html')

def Logros(request):

    return render(request ,'wiki/Logros.html')

def Lugares(request):

    return render(request ,'wiki/Lugares.html')

def Micuenta(request):
    
    return render(request ,'wiki/Micuenta.html')

def Recuperarcontra(request):

    return render(request ,'wiki/Recuperarcontra.html')

def Registrarse(request):

    return render(request ,'wiki/Registrarse.html')

def Admin(request):

    return render(request , 'wiki/Admin.html')


def Vcontra(request):
    
    return render(request , 'wiki/VerificarContra.html')

def ModificarC(request):

    return render(request, 'wiki/ModificarCuenta.html')

def FormularioTablas(request):

    return render(request, 'wiki/FormularioTablas.html')

def registrar_usuario(request):
    nombre_u = request.POST['validationCustom01']
    apellido_u = request.POST['apellido']
    nomusuario_u = request.POST['nomusuario']
    avatar_u = request.FILES['foto_u']
    correo_u = request.POST['validationCustom04']
    clave_u = request.POST['contra1']


    estado_u = Estado.objects.get(id_estado = 4)
    tipousuario2 = TipoUsuario.objects.get(id_tipo = 2)
    
    Usuario.objects.create(id_usuario = nomusuario_u, nombre = nombre_u, apellido = apellido_u, correo = correo_u, clave = clave_u, foto = avatar_u, estado = estado_u, tipousuario = tipousuario2)
    messages.success(request,'Usuario Registrado')
    return redirect('menuprincipal')



def listado(request):
    listadoUsuario = Usuario.objects.all()
    return render(request , 'wiki/Admin.html',{"listados" : listadoUsuario})

def penalizarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    estadoU=Estado.objects.get(id_tipo = 2)
    Usuario.save()
    messages.success(request, 'Usuario baneado')

    return redirect('listado')

def borrarUsuario(request, id_usuario):
    eliminar = Usuario.objects.get(id_usuario = id_usuario)
    eliminar.delete()
    messages.success(request, 'Usuario borrado')

    return redirect('listado')


def modificarC2(request):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    nomusuario_u = request.POST['nomusuario']
    avatar_u = request.FILES['foto']
    correo_u = request.POST['correo']
    clave_u = request.POST['Clave1']
    clave_u2 = request.POST['Clave2']

    usuario = Usuario.objects.get(id_usuario = nomusuario_u)
    usuario.nombre = nombre_u
    usuario.apellido = apellido_u
    usuario.foto = avatar_u
    usuario.correo = correo_u
    usuario.clave = clave_u
    usuario.clave = clave_u2

    usuario.save()

    messages.success(request, 'Usuario Modificado')
    return redirect('Micuenta')







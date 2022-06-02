from cgitb import html
from turtle import update
from django.shortcuts import render, redirect
from .models import Comentario, Tabla, TipoUsuario, Usuario,Estado
from django.contrib import messages
import datetime
# Create your views here.

def menuprincipal(request):

    return render(request ,'wiki/menuprincipal.html')

def Animales(request):

    return render(request ,'wiki/Animales.html')

def Armas(request):

    listadoTabla = Tabla.objects.filter(categoria = 1)
    
    return render(request , 'wiki/Armas.html',{"listados" : listadoTabla})

def Construcciones(request):

    return render(request ,'wiki/Construcciones.html')

def Consumibles(request):

    return render(request ,'wiki/Consumibles.html')

def Enemigos(request):

    listadoTabla = Tabla.objects.filter(categoria = 2)
    
    return render(request , 'wiki/Enemigos.html',{"listados" : listadoTabla})

def Flora(request):

    return render(request ,'wiki/Flora.html')

def forowiki(request):

    listadoForo = Comentario.objects.all()
    
    return render(request , 'wiki/forowiki.html',{"listados" : listadoForo})

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


    estado_u = Estado.objects.get(id_estado = 1)
    tipousuario2 = TipoUsuario.objects.get(id_tipo = 2)
    
    Usuario.objects.create(id_usuario = nomusuario_u, nombre = nombre_u, apellido = apellido_u, correo = correo_u, clave = clave_u, foto = avatar_u, estado = estado_u, tipousuario = tipousuario2)
    messages.success(request,'Usuario Registrado')
    return redirect('menuprincipal')

def ini_sesion(request):
    usuario1 = request.POST['usuariof']
    contra = request.POST['contrasena']
    try:
        usuario2 = Usuario.objects.get(id_usuario = usuario1 , clave = contra)
        if(usuario2.tipousuario.id_tipo == 2):
            return redirect ('menuprincipal')
        else:
            return redirect ('Registrarse')
    except:
        messages.error(request, 'El Usuario y/o contraseñas son incorrectos')
        return redirect ('inicio-sesion')

def listado(request):
    listadoUsuario = Usuario.objects.all()
    return render(request , 'wiki/Admin.html',{"listados" : listadoUsuario})

def listadoForo(request):
    listadoComentario = Comentario.objects.all()
    return render(request , 'wiki/Admin.html',{"listadosForo" : listadoComentario})

def penalizarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    if usuario.estado == 1:
        usuario.estado = 2
        Usuario.save()
        messages.success(request, 'Usuario baneado')
    elif usuario.estado == 2:
        usuario.estado = 1
        Usuario.save()
        messages.success(request, 'Usuario desbaneado')

    return redirect('listado')

def borrarUsuario(request, id_usuario):
    eliminar = Usuario.objects.get(id_usuario = id_usuario)
    eliminar.delete()
    messages.success(request, 'Usuario borrado')

    return redirect('listado')

def borrarContenido(request, id_tema):
    eliminar = Tabla.objects.get(id_tema = id_tema)
    eliminar.delete()
    messages.success(request, 'Contenido borrado')

    return redirect('Armas')

def registroTabla(request):
    categoriat = request.POST['categoria']
    fotot = request.FILES['foto']
    nomDato = request.POST['nombreDato']
    tipoDato = request.POST['tipodato']
    desDato = request.POST['descripcion']
    fecDato = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    estadoDato = Estado.objects.get(id_estado = 1)

    Tabla.objects.create(categoria = categoriat, foto = fotot, nom_dato = nomDato, tipodato = tipoDato, descripcion = desDato, f_creacion = fecDato, estado = estadoDato)
    messages.success(request,'Dato registrado')
    return redirect('menuprincipal')

def borrarComentario(request, id_comentario):
    eliminar = Comentario.objects.get(id_comentario = id_comentario)
    eliminar.delete()
    messages.success(request, 'Comentario borrado')

    return redirect('forowiki')


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

   
    Usuario.objects.update(id_usuario = nomusuario_u, nombre = nombre_u, apellido = apellido_u, correo = correo_u, clave = clave_u, foto = avatar_u)
    usuario.save()
    messages.success(request, 'Usuario Modificado')
    return redirect('Micuenta')



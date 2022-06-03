from cgitb import html
import re
from turtle import update
from django.shortcuts import render, redirect
from .models import Categoria, Comentario, Tabla, TipoUsuario, Usuario,Estado
from django.contrib import messages
import datetime
# Create your views here.

def menuprincipal(request):

    return render(request ,'wiki/menuprincipal.html')

def Animales(request):

    listadoTabla = Tabla.objects.filter(categoria = 3)

    return render(request ,'wiki/Animales.html', {"listados" : listadoTabla})

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
    
    listadoTabla = Tabla.objects.filter(categoria = 4)

    return render(request , 'wiki/Flora.html',{"listados" : listadoTabla})


def forowiki(request):

    listadoForo = Comentario.objects.all()
    
    return render(request , 'wiki/forowiki.html',{"listados" : listadoForo})

def Historia(request):

    return render(request ,'wiki/Historia.html')

def inicio_sesion(request):

    return render(request ,'wiki/inicio-sesion.html')

def Logros(request):

    listadoTabla = Tabla.objects.filter(categoria = 5)

    return render(request , 'wiki/Logros.html',{"listados" : listadoTabla})

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

def ModificarC(request, id_usuario):

    listadoTabla = Tabla.objects.get(id_usuario = id_usuario)

    return render(request, 'wiki/ModificarCuenta.html', {"listados":listadoTabla})

def FormularioTablas(request):

    categoria1 = Categoria.objects.all()

    contexto = {
        "categoria":categoria1
    }

    return render(request, 'wiki/FormularioTablas.html', contexto)

def EditarTablas(request, id_tema):
    listadoTabla = Tabla.objects.get(id_tema = id_tema)
    categoria1 = Categoria.objects.all()

    contexto = {
        "categoria":categoria1
    }
    return render(request ,'wiki/EditarTablas.html', {"listados":listadoTabla}, contexto)

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
        elif(usuario2.tipousuario.id_tipo == 1):
            return redirect ('Admin')
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
    usut = request.POST['usuarioa']
    categoriat = request.POST['categoria']
    categoriat2 = Categoria.objects.get(id_categoria = categoriat)
    fotot = request.FILES['foto']
    nomDato = request.POST['nombreDato']
    tipoDato = request.POST['tipodato']
    desDato = request.POST['descripcion']
    fecDato = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    estadoDato = Estado.objects.get(id_estado = 1)

    Tabla.objects.create(usuario = usut,categoria = categoriat2, foto = fotot, nom_dato = nomDato, tipodato = tipoDato, descripcion = desDato, f_creacion = fecDato, estado = estadoDato)
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

def modificarTabla(request):
    usut = request.POST['usuarioa']
    id_tema = request.POST['id_t']
    categoriat = request.POST['categoria']
    categoriat2 = Categoria.objects.get(id_categoria = categoriat)
    if(request.POST.get('foto')):
        fotot = request.FILES['foto']
        listadoTabla.foto = fotot

    nodato = request.POST['nombreDato']
    tipoDato = request.POST['tipodato']
    Descripcion = request.POST['descripcion']
    fech = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    listadoTabla = Tabla.objects.get(id_tema = id_tema)

    listadoTabla.usuario = usut
    listadoTabla.categoria = categoriat2
    listadoTabla.nom_dato = nodato
    listadoTabla.tipodato = tipoDato
    listadoTabla.descripcion = Descripcion
    listadoTabla.f_creacion = fech
    listadoTabla.save()

    return redirect('menuprincipal')

def aniadirComentario(request):
    usut = request.POST('usuarioa')
    dtema = request.POST('tema')
    comentariou = request.POST('Comentario')
    fcreacion = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    estadoDato = Estado.objects.get(id_estado = 1)

    Comentario.objects.create(usuario = usut, titulo_com = dtema, texto = comentariou, f_creacion = fcreacion, estado = estadoDato)
    messages.success(request,'Comentario añadido')
    return redirect('forowiki')

from cgitb import html
from multiprocessing import context
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


def forowiki(request,id_usuario):

    listadoForo = Comentario.objects.all()
    usu = Usuario.objects.get(id_usuario=id_usuario)
    contexto={
        "usuario":usu,
        "listados":listadoForo
    }
    return render(request ,'wiki/forowiki.html',contexto)

def Historia(request):

    return render(request ,'wiki/Historia.html')

def inicio_sesion(request):

    return render(request ,'wiki/inicio-sesion.html')

def Logros(request):

    listadoTabla = Tabla.objects.filter(categoria = 5)

    return render(request , 'wiki/Logros.html',{"listados" : listadoTabla})

def Lugares(request):

    return render(request ,'wiki/Lugares.html')

def Micuenta(request, id_usuario):
    cuenta = Usuario.objects.get(id_usuario = id_usuario)

    return render(request ,'wiki/Micuenta.html',{"usuario":cuenta})

def Recuperarcontra(request):

    return render(request ,'wiki/Recuperarcontra.html')

def Registrarse(request):

    return render(request ,'wiki/Registrarse.html')

def Admin(request):
    listadoUsuario = Usuario.objects.all()
    return render(request , 'wiki/Admin.html',{"listados" : listadoUsuario})


def Vcontra(request):
    
    return render(request , 'wiki/VerificarContra.html')

def ModificarC(request, id_usuario):

    listadoTabla = Usuario.objects.get(id_usuario = id_usuario)

    return render(request, 'wiki/ModificarCuenta.html', {"usuario":listadoTabla})

def FormularioTablas(request):

    categoria1 = Categoria.objects.all()
    usuariost = Usuario.objects.all()

    contexto = {
        "categoria":categoria1,
        "usuariop":usuariost
    }

    return render(request, 'wiki/FormularioTablas.html',contexto)

def EditarTablas(request, id_tema):
    listadoTabla = Tabla.objects.get(id_tema = id_tema)
    categoria1 = Categoria.objects.all()

    contexto = {
        "categoria":categoria1,
        "listados":listadoTabla
    }
    return render(request ,'wiki/EditarTablas.html', contexto)

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
        
        contexto ={
            "usuario":usuario2
        }
        if(usuario2.tipousuario.id_tipo == 2):
            return render (request,'wiki/menuprincipal.html',contexto)
        elif(usuario2.tipousuario.id_tipo == 1):
            return render (request,'wiki/Admin.html',contexto)
        else:
            
            return redirect ('menuprincipal')
    except:
        messages.error(request, 'El Usuario y/o contraseñas son incorrectos')
        return redirect (request,'wiki/inicio-sesion.html',contexto)


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

    return redirect('menuprincipal')

def registroTabla(request,id_usuario):
    usut = request.POST.get('usuarioa')

    categoriat = request.POST.get('categoria')
    cat2 = Categoria.objects.get(id_categoria=categoriat)
    fotot = request.FILES.get('foto')
    nomDato = request.POST.get('nombreDato')
    tipoDato = request.POST.get('tipodato')
    desDato = request.POST.get('descripcion')
    fecDato = datetime.datetime.now()

    estadoDato = Estado.objects.get(id_estado = 1)

    contexto={
        "usuario":id_usuario
    }
    Tabla.objects.create(usuario = usut,categoria = cat2, foto = fotot, nom_dato = nomDato, tipodato = tipoDato, descripcion = desDato, f_creacion = fecDato, estado = estadoDato)
    messages.success(request,'Dato registrado')
    return render(request,'wiki/menuprincipal.html',contexto)

def borrarComentario(request, id_comentario):
    eliminar = Comentario.objects.get(id_comentario = id_comentario)
    eliminar.delete()
    messages.success(request, 'Comentario borrado')

    return redirect('forowiki')


def modificarC2(request,id_usuario):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    nomusuario_u = request.POST['nomusuario']
    avatar_u = request.FILES['foto']
    correo_u = request.POST['correo']
    clave_u = request.POST['Clave1']

    contexto ={
            "usuario":id_usuario
        }

    usuario = Usuario.objects.get(id_usuario = nomusuario_u)
    usuario.nombre = nombre_u
    usuario.apellido = apellido_u
    usuario.foto = avatar_u
    usuario.correo = correo_u
    usuario.clave = clave_u


   

    usuario.save()
    messages.success(request,'Usuario Modificado')
    return render(request,'wiki/Micuenta.html',contexto)

def modificarTabla(request,id_usuario):
    usut = request.POST['usuarioa']
    id_tema = request.POST['idt']
    categoriat = request.POST['categoria']
    categoriat2 = Categoria.objects.get(id_categoria = categoriat)
    if(request.POST.get('foto')):
        fotot = request.FILES['foto']
        listadoTabla.foto = fotot

    nodato = request.POST['nombreDato']
    tipoDato = request.POST['tipodato']
    Descripcion = request.POST['descripcion']
    fech = datetime.datetime.now()

    contexto ={
            "usuario":id_usuario
        }

    listadoTabla = Tabla.objects.get(id_tema = id_tema)

    listadoTabla.usuario = usut
    listadoTabla.categoria = categoriat2
    listadoTabla.nom_dato = nodato
    listadoTabla.tipodato = tipoDato
    listadoTabla.descripcion = Descripcion
    listadoTabla.f_creacion = fech
    listadoTabla.save()

    return render(request,'wiki/menuprincipal.html',contexto)

def aniadirComentario(request,id):
    dtema = request.POST.get('tema')
    comentariou = request.POST.get('Comentario')
    usut = Usuario.objects.get(id_usuario = id)
    estadoDato = Estado.objects.get(id_estado = 1)

    contexto ={"usuario":usut}
    
    existe = None
    try:
        existe = Comentario.objects.get (texto =comentariou)
        messages.error(request,'El Comentario ya existe')
        return redirect('Foro')
    
    except:
        Comentario.objects.create(titulo_com = dtema,f_creacion = datetime.datetime.now(), texto = comentariou, estado = estadoDato,usuario = usut)
        messages.success(request,'Comentario añadido')
        return render(request,'wiki/forowiki.html',contexto)

    


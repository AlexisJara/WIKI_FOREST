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

def menuprincipal2(request, usuario):
    usuario = Usuario.objects.get(id_usuario = usuario)
    contexto = {"usuario":usuario}
    return render(request ,'wiki/menuprincipal.html', contexto)

def Animales(request,usuario):
    usuario = Usuario.objects.get(id_usuario = usuario)
    listadoTabla = Tabla.objects.filter(categoria = 3)
    contexto = {"listados" : listadoTabla, "usuario" : usuario}

    return render(request ,'wiki/Animales.html',contexto )

def Armas(request,usuario):
    usuario = Usuario.objects.get(id_usuario = usuario)

    listadoTabla = Tabla.objects.filter(categoria = 1)
    contexto = {"listados" : listadoTabla, "usuario" : usuario}
    
    return render(request , 'wiki/Armas.html',contexto)

def Construcciones(request):

    return render(request ,'wiki/Construcciones.html')

def Consumibles(request):

    return render(request ,'wiki/Consumibles.html')

def Enemigos(request,usuario):

    usuario = Usuario.objects.get(id_usuario = usuario)
    listadoTabla = Tabla.objects.filter(categoria = 2)
    contexto = {"listados" : listadoTabla, "usuario" : usuario}
    
    return render(request,'wiki/Enemigos.html',contexto)

def Flora(request,usuario):
    usuario = Usuario.objects.get(id_usuario = usuario)
    listadoTabla = Tabla.objects.filter(categoria = 4)
    contexto = {"listados":listadoTabla,"usuario" : usuario}

    return render(request , 'wiki/Flora.html',contexto)


def forowiki(request,usuario):

    listadoForo = Comentario.objects.all()
    usu = Usuario.objects.get(id_usuario=usuario)
    contexto={"usuario":usu,"listados":listadoForo}
    return render(request ,'wiki/forowiki.html',contexto)

def Historia(request):

    return render(request ,'wiki/Historia.html')

def inicio_sesion(request):

    return render(request ,'wiki/inicio-sesion.html')

def Logros(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    listadoTabla = Tabla.objects.filter(categoria = 5)
    contexto = {"listados":listadoTabla,"usuario" : usuario}

    return render(request , 'wiki/Logros.html',contexto)

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

def FormularioTablas(request,usuario):

    categoria1 = Categoria.objects.all()
    usuariost = Usuario.objects.get(id_usuario = usuario)
    contexto = { "categoria":categoria1,"usuario":usuariost}

    return render(request, 'wiki/FormularioTablas.html',contexto)

def EditarTablas(request, id_tema,usuario):
    listadoTabla = Tabla.objects.get(id_tema = id_tema)
    usuario = Usuario.objects.get(id_usuario = usuario)
    categoria1 = Categoria.objects.all()

    contexto = {"categoria":categoria1,"listados":listadoTabla,"usuario":usuario}

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

        if(usuario2.tipousuario.id_tipo == 1):
            contexto = {"usuario":usuario2}
            return render (request,'wiki/menuprincipal2.html',contexto)
        else:
            if(usuario2.estado.id_estado == 2):
                messages.error(request, 'El usuario que ingresaste se encuentra baneado')
                return redirect ('Inicio-sesion')
            else:
                contexto = {"usuario":usuario2}
                return render (request,'wiki/menuprincipal.html',contexto)
            
    except:
        messages.error(request, 'El Usuario y/o contraseñas son incorrectos')
        return redirect ('Inicio-sesion')


def listado(request):
    listadoUsuario = Usuario.objects.all()
    return render(request , 'wiki/Admin.html',{"listados" : listadoUsuario})

def listadoForo(request):
    listadoComentario = Comentario.objects.all()
    return render(request , 'wiki/Admin.html',{"listadosForo" : listadoComentario})

def penalizarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    if usuario.estado.id_estado == 1:
        usuario.estado = Estado.objects.get(id_estado = 2)
        usuario.save()
        messages.success(request, '---Usuario baneado exitosamente---')
    elif usuario.estado.id_estado == 2:
        usuario.estado = Estado.objects.get(id_estado = 1)
        usuario.save()
        messages.success(request, '---Usuario desbaneado exitosamente---')

    return redirect('listado')

def borrarUsuario(request, id_usuario):
    eliminar = Usuario.objects.get(id_usuario = id_usuario)
    eliminar.delete()
    messages.success(request, '---Usuario borrado exitosamente---')

    return redirect('listado')

def borrarContenido(request, id_tema, usuario):
    usuario1 = Usuario.objects.get(id_usuario = usuario)
    eliminar = Tabla.objects.get(id_tema = id_tema)
    eliminar.delete()

    contexto = {"usuario":usuario1}
    messages.success(request,'---Contenido borrado exitosamente---')
    return render(request, 'wiki/menuprincipal.html', contexto)

def registroTabla(request,usuario):
    usuario1 = Usuario.objects.get(id_usuario = usuario)
    categoriat = request.POST.get('categoria')
    cat2 = Categoria.objects.get(id_categoria=categoriat)
    fotot = request.FILES.get('foto')
    nomDato = request.POST.get('nombreDato')
    tipoDato = request.POST.get('tipodato')
    desDato = request.POST.get('descripcion')
    fecDato = datetime.datetime.now()

    estadoDato = Estado.objects.get(id_estado = 1)

    contexto={"usuario":usuario1}

    Tabla.objects.create(usuario = usuario1,categoria = cat2, foto = fotot, nom_dato = nomDato, tipodato = tipoDato, descripcion = desDato, f_creacion = fecDato, estado = estadoDato)
    messages.success(request,'---Dato registrado exitosamente---')
    return render(request,'wiki/menuprincipal.html',contexto)

def borrarComentario(request, id_comentario,usuario):
    usuario1 = Usuario.objects.get(id_usuario = usuario)
    eliminar = Comentario.objects.get(id_comentario = id_comentario)
    eliminar.delete()
    contexto={"usuario":usuario1}

    messages.success(request, '---Comentario borrado exitosamente---')

    return render(request,'wiki/menuprincipal.html',contexto)


def modificarC2(request,usuario):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    nomusuario_u = request.POST['nomusuario']
    avatar_u = request.FILES['foto']
    correo_u = request.POST['correo']
    clave_u = request.POST['Clave1']

    
    usuario = Usuario.objects.get(id_usuario = nomusuario_u)
    usuario.nombre = nombre_u
    usuario.apellido = apellido_u
    usuario.foto = avatar_u
    usuario.correo = correo_u
    usuario.clave = clave_u
    contexto ={
            "usuario":usuario
        }

   

    usuario.save()
    messages.success(request,'Usuario Modificado exitosamente')
    return render(request,'wiki/Micuenta.html',contexto)

def modificarTabla(request,usuario):
    usuario1= Usuario.objects.get(id_usuario = usuario)
    usut = usuario1
    id_tema = request.POST['idt']
    listadoTabla = Tabla.objects.get(id_tema = id_tema)
    categoriat = request.POST['categoria']
    categoriat2 = Categoria.objects.get(id_categoria = categoriat)
    nodato = request.POST['nombreDato']
    tipoDato = request.POST['tipodato']
    Descripcion = request.POST['descripcion']
    fech = datetime.datetime.now()
    if (request.FILES.get("foto")):
        fotot = request.FILES['foto']
        listadoTabla.foto = fotot
    contexto ={"usuario":usuario1}

    listadoTabla.usuario = usut
    listadoTabla.categoria = categoriat2
    listadoTabla.nom_dato = nodato
    listadoTabla.tipodato = tipoDato
    listadoTabla.descripcion = Descripcion
    listadoTabla.f_creacion = fech
    listadoTabla.save()

    messages.success(request,'---Contenido modificado exitosamente---')
    return render(request,'wiki/menuprincipal.html',contexto)

def aniadirComentario(request,id):
    dtema = request.POST['tema']
    comentariou = request.POST['Comentario']
    usut = Usuario.objects.get(id_usuario = id)
    estadoDato = Estado.objects.get(id_estado = 1)
    fechaa = datetime.datetime.now()

    contexto ={"usuario":usut}

    Comentario.objects.create(titulo_com = dtema,f_creacion = fechaa, texto = comentariou, estado = estadoDato,usuario = usut)
    messages.success(request,'---Comentario añadido exitosamente---')
    return render(request,'wiki/menuprincipal.html',contexto)

    


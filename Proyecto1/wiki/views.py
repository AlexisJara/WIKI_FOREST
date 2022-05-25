from cgitb import html
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

    estado_u = Estado.objects.get(id_estado = 1)
    tipousuario2=TipoUsuario.objects.get(id_tipo = 2)
    existe = None
    try:
        existe = Usuario.objects.get(id_usuario = nomusuario_u)
        messages.error(request,'El usuario existe')
        return redirect ('registro')
    except:
        Usuario.objects.create(id_usuario = nomusuario_u, nombre = nombre_u, apellido = apellido_u, correo = correo_u, clave = clave_u, foto = avatar_u, Estado = estado_u, TipoUsuario = tipousuario2  )
        return redirect('registrarse')




def listado(request):
    listadoUsuario = Usuario.objects.get("id_usuario","correo","estado")
    contexto = {"listados" : listadoUsuario}
    return render(request , 'wiki/Admin.html',contexto)

def penalizarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    usuario.estado = 2
    Usuario.save()
    messages.success('Usuario baneado')

    return redirect(request, 'listado')

def borrarUsuario(request, id_usuario):
    eliminar = Usuario.objects.get(id_usuario = id_usuario)
    eliminar.delete()
    messages.success(request, 'Usuario borrado')

    return redirect('listado')



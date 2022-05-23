from django.shortcuts import render, redirect
from Proyecto1.wiki.models import Estado, TipoUsuario
from models import Usuario, TipoUsuario

# Create your views here.

def menuprincipal(request):

    return render(request ,'wiki/menuprincipal.html')

def Admin(request):

    return render(request ,'wiki/Admin.html')

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

def Registrarse(request):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    usuario_u = request.POST['nomusuario']
    img_foto = request.FILES['foto']
    email_u = request.POST['correo']
    contra_u = request.POST['contra1']

    tipo_u = TipoUsuario.objects.get(id_tipo = 1)
    estado_u = Estado.objects.get(id_estado = 1)

    Usuario.objects.create(nombre = nombre_u, apellido = apellido_u, id_usuario = usuario_u, foto = img_foto, correo = email_u, clave = contra_u, tipousuario = tipo_u,estado = estado_u)

    return redirect('Registrarse/')
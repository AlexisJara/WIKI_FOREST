from django.shortcuts import render

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
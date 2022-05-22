from pyexpat import model
from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    id_tipo = models.AutoField(primary_key=True, verbose_name='Id de tipo usuario')
    nombre = models.CharField(max_length=20, verbose_name='Nombre del tipo usuario', blank=False)

    def __str__(self) :
        return self.nombre

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, verbose_name='Id del estado')
    nombre = models.CharField(max_length=20, verbose_name='Nombre del estado')

    def __str__(self) :
        return self.nombre

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=12,verbose_name='id del usuario', blank=False)
    nombre = models.CharField(max_length=20, verbose_name='Nombre del usuario', blank=False)
    apellido = models.CharField(max_length=20, verbose_name='Apellido del usuario', blank=False)
    correo = models.CharField(max_length=30, verbose_name='Mail del usuario', blank=False)
    clave = models.CharField(max_length=20, verbose_name='Clave del usuario', blank=False)
    foto = models.ImageField(null=True, blank=False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    tipousuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    def __str__(self) :
        return self.id_usuario


class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True, verbose_name='Mensaje que se le envia al usuario')
    f_creacion = models.DateTimeField(verbose_name='Fecha de la creacion', blank=False)
    contenido = models.CharField(max_length=250, verbose_name='contenido del mensaje', blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipousuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self) :
        return self.contenido

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, verbose_name='Id de la categoria')
    nombre = models.CharField(max_length=20, verbose_name='Nombre de la categoria')

    def __str__(self) :
        return self.nombre

class Tabla(models.Model):
    id_tema = models.AutoField(primary_key=True, verbose_name='Id del tema')
    nom_dato = models.CharField(max_length=50, verbose_name='nombre del enemigo', blank=False)
    foto = models.ImageField(null=True)
    tipodato = models.CharField(max_length=30, blank=False)
    descripcion = models.CharField(max_length=250, verbose_name='contenido del comentario del foro', blank=False)
    f_creacion = models.DateTimeField(verbose_name='fecha de creacion', blank=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    tipousuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) :
        return self.nom_dato

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True, verbose_name='Id del comentario')
    f_creacion = models.DateTimeField(verbose_name='fecha de la creacion', blank=False)
    texto = models.CharField(max_length=250, verbose_name='descripcion del comentario', blank=False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipousuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) :
        return self.texto





    






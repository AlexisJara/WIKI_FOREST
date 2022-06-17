from rest_framework import serializers
from wiki.models import Tabla,Usuario,Comentario

#Tabla contenido
class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = ['id_tema','foto','nom_dato','descripcion','tipodato','f_creacion','estado','usuario','categoria']

class TablaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = ['id_tema','foto','nom_dato','descripcion','tipodato','f_creacion','estado','usuario','categoria']
##################################
#Tabla Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre','apellido','correo','clave','foto','estado','tipousuario']

class UsuarioSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre','apellido','correo','clave','foto','estado','tipousuario']
######################################
#Comentario foro
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id_comentario','titulo_com','f_creacion','texto','estado','usuario']

class ComentarioSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id_comentario','titulo_com','f_creacion','texto','estado','usuario']
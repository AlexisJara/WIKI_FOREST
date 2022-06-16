from rest_framework import serializers
from wiki.models import Tabla,Usuario

class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = ['id_tema','foto','nom_dato','descripcion','tipodato','f_creacion','estado','usuario','categoria']

class TablaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = ['id_tema','foto','nom_dato','descripcion','tipodato','f_creacion','estado','usuario','categoria']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre','apellido','correo','clave','foto','estado','tipousuario']

class UsuarioSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre','apellido','correo','clave','foto','estado','tipousuario']
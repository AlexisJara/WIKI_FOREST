from rest_framework import serializers
from wiki.models import Tabla,Comentario

class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = ['nomdato','descripcion','f_creacion']

class TablaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = ['nomdato','descripcion','f_creacion','foto']
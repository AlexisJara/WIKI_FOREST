from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


from .serializers import TablaSerializer,TablaSerializer2,UsuarioSerializer,UsuarioSerializer2,ComentarioSerializer,ComentarioSerializer2
from wiki.models import Tabla,Usuario,Comentario

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt

#tablas WIKI api#####################################
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_tablas(request):
    if request.method == 'GET':
        tablas = Tabla.objects.all()
        serializer = TablaSerializer(tablas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = TablaSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarC(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = TablaSerializer2(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlC(request,id):
    try:
        t = Tabla.objects.get(id_tema = id)
    except Tabla.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TablaSerializer2(t)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = TablaSerializer2(t,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        t.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
############################################################

#Usuario#####################################
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_usuario(request):
    if request.method == 'GET':
        u = Usuario.objects.all()
        serializer = UsuarioSerializer(u,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarUsuario(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer2(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlUsuario(request,id):
    try:
        us = Usuario.objects.get(id_usuario = id)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer2(us)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer2(us,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        us.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
######################################################################
#Comentario
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_foro(request):
    if request.method == 'GET':
        u = Comentario.objects.all()
        serializer = ComentarioSerializer(u,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ComentarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarComentario(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ComentarioSerializer2(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlForo(request,id):
    try:
        us = Comentario.objects.get(id_comentario = id)
    except Comentario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ComentarioSerializer2(us)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ComentarioSerializer2(us,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        us.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


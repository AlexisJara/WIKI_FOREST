from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import TablaSerializer,TablaSerializer2
from wiki.models import Tabla

# Create your views here.
@csrf_exempt

@api_view(['GET','POST'])
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
def controlC(request,codigo):
    try:
        t = Tabla.objects.get(id_tema = codigo)
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
from django.urls import path
from rest_wiki.views import lista_tablas,agregarC,controlC,lista_usuario,agregarUsuario,controlUsuario,lista_foro,agregarComentario,controlForo
from rest_wiki.viewsLogin import login

urlpatterns = [
    #lista tabla wiki
    path('lista_tablas/',lista_tablas,name="lista_tablas"),
    path('agregarC/',agregarC,name="agregarC"),
    path('controlC/<id>',controlC,name="controlC"),
    path('login/',login,name="login"),

    #usuarios
    path('lista_usuario/',lista_usuario,name="lista_usuario"),
    path('agregarUsuario/',agregarUsuario,name="agregarUsuario"),
    path('controlUsuario/<id>',controlUsuario,name="controlUsuario"),

    #Comentario
    path('lista_foro/',lista_foro,name="lista_foro"),
    path('agregarComentario/',agregarComentario,name="agregarComentario"),
    path('controlForo/<id>',controlForo,name="controlForo"),
]
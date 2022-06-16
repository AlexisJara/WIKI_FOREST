from django.urls import path
from rest_wiki.views import lista_tablas,agregarC,controlC
from rest_wiki.viewsLogin import login

urlpatterns = [
    path('lista_tablas/',lista_tablas,name="lista_tablas"),
    path('agregarC/',agregarC,name="agregarC"),
    path('controlC/<codigo>',controlC,name="controlC"),
    path('login/',login,name="login"),
]
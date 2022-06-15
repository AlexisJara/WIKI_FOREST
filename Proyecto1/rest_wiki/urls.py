from django.urls import path
from rest_wiki.views import lista_tablas,agregarC,controlC

urlpatterns = [
    path('lista_tablas/',lista_tablas,name="lista_tablas"),
    path('agregarC/',agregarC,name="agregarC"),
    path('controlC/<codigo>',controlC,name="controlC"),
]
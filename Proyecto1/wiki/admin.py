from django.contrib import admin
from .models import TipoUsuario,Estado,Usuario,Mensaje,Categoria,Tabla,Comentario
# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Estado)
admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Categoria)
admin.site.register(Tabla)
admin.site.register(Comentario)
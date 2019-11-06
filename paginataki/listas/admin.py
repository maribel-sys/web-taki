from django.contrib import admin
from .models import Mercado,Productos,Recetario,Recuerdame
# Register your models here.

admin.site.register(Productos)
admin.site.register(Mercado)
admin.site.register(Recetario)
admin.site.register(Recuerdame)

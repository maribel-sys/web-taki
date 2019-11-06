from django.shortcuts import render
from .models import Mercado,Productos,Recetario,Recuerdame

# Create your views here.

def mercado(request):
  mercados = Mercado.objects.all()
  return render(request, "listas/mercado.html", {'mercados': mercados })

def listadeproducto(request):
  productos = Productos.objects.all()
  return render(request, "listas/listadeproducto.html", {'productos':productos })

def recetario(request):
  recetario = Recetario.objects.all()
  return render(request, "listas/recetario.html", {'recetario': recetario })

def recuerdame(request):
  recordatorio = Recuerdame.objects.all()
  return render(request, "listas/recuerdame.html", {'recordatorio': recordatorio })
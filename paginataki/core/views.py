from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
  
   return render(request, "core/home.html") 

def acercade(request):
  
  return render(request, "core/acercade.html")

def listasproyecto(request):
  
  return render(request,"core/listasproyecto.html")

def tablas(request):
  
  return render(request,"core/tablas.html")










  

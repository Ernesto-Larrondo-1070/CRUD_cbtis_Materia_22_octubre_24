from django.shortcuts import render
from .models import Materia
# Create your views here.
def inicio_vista(request):
    # obtener todos los regristros de la tabla materia
    listadoMateria= Materia.objects.all()
    return render(request,"gestionarMateria.html",{"lasmaterias":listadoMateria})

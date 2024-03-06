from django.shortcuts import render, redirect
from datetime import datetime
from .models import Task
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Create your views here.
def list_task(request):
    task = Task.objects.all()
    return render(request,'list_task.html', {"task": task})



def create_task(request):
    task = Task(    
    carnet = request.POST['carnet'],
    nombres = request.POST['nombres'],
    apellidos = request.POST['apellidos'],
    correoelectronico = request.POST['correoelectronico'],
    fechaNacimiento =request.POST['fechaNacimiento']
    )

    task.save()
    return redirect('/task/')
 


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/task/')
    




# Create your views here.
def cont(request):


    tasks = Task.objects.all()
    count = tasks.count()  # Contar la cantidad total de registros

    # Contar registros mayores y menores de 18 años
    mayor_count = 0
    menor_count = 0
    for task in tasks:
        if (datetime.now().year - task.fechaNacimiento.year) >= 18:
            mayor_count += 1
        else:
            menor_count += 1

    return render(request, 'report.html', { 'count': count, 'mayor_count': mayor_count, 'menor_count': menor_count})


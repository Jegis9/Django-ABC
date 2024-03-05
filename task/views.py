from django.shortcuts import render, redirect

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
    




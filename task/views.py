from django.shortcuts import render, redirect
from datetime import datetime
from .models import Task
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.views.decorators.http import require_POST


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
 

def editarTask(request, task_id):
    # Obtener la tarea por su ID
    task = get_object_or_404(Task, id=task_id)
    
    # Actualizar los datos de la tarea con los datos recibidos del formulario
    carnet = request.POST.get('carnet')
    nombres = request.POST.get('nombres')
    apellidos = request.POST.get('apellidos')
    correoelectronico = request.POST.get('correo')
    fechaNacimiento = request.POST.get('fecha')
    
    # Verificar si los campos no son null antes de asignarlos a la instancia de Task
    if carnet is not None:
        task.carnet = carnet
    if nombres is not None:
        task.nombres = nombres
    if apellidos is not None:
        task.apellidos = apellidos
    if correoelectronico is not None:
        task.correoelectronico = correoelectronico
    if fechaNacimiento is not None:
        task.fechaNacimiento = fechaNacimiento
    
    # Guardar los cambios en la base de datos
    task.save()
    
    # Redirigir a alguna página de confirmación o a la misma página de edición
    return redirect('editarTask', task_id=task_id)




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


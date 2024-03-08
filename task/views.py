from django.shortcuts import render, redirect
from datetime import datetime
from .models import Task
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponseNotAllowed

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
 

""" def editarTask(request, task_id):

    if request.method == 'POST':

        if require_POST.get('carnet') and require_POST.get('nombres') and require_POST.get('apellidos') and require_POST.get('correo') and require_POST.get('fecha'):
        task = Task()
        task.carnet = request.POST.get('carnet')
        task.nombres = request.POST.get('nombres')
        task.apellidos = request.POST.get('apellidos')
        task.correoelectronico = request.POST.get('correo')
        task.fechaNacimiento = request.POST.get('fecha')
        

        task.save()
        return redirect('/task/')

"""

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.carnet = request.POST.get('carnet')
        task.nombres = request.POST.get('nombres')
        task.apellidos = request.POST.get('apellidos')
        task.correoelectronico = request.POST.get('correoelectronico')
        task.fechaNacimiento = request.POST.get('fechaNacimiento')
        task.save()
        return redirect('/task/') 

    context = {
        'task': task,
    }
    return render(request, 'edit_task.html', context)



def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/task/')
    



import json
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render

def report(request):
    personas = Task.objects.all()

    # Lista para almacenar las edades
    edades = []

    # Calcular las edades y agregarlas a la lista
    for persona in personas:
        edad = datetime.now().year - persona.fechaNacimiento.year
        edades.append(edad)

    # Procesar las edades para obtener los grupos de edades
    grupos_edades = {
        '0-9': 0,
        '10-19': 0,
        '20-29': 0,
        '30-39': 0,
        '40-49': 0,
        '50-59': 0
    }

    for edad in edades:
        if edad >= 0 and edad <= 9:
            grupos_edades['0-9'] += 1
        elif edad >= 10 and edad <= 19:
            grupos_edades['10-19'] += 1
        elif edad >= 20 and edad <= 29:
            grupos_edades['20-29'] += 1
        elif edad >= 30 and edad <= 39:
            grupos_edades['30-39'] += 1
        elif edad >= 40 and edad <= 49:
            grupos_edades['40-49'] += 1
        elif edad >= 50 and edad <= 59:
            grupos_edades['50-59'] += 1
        else:
            grupos_edades['90+'] += 1

    # Convertir el diccionario a JSON
    rangos_edades_json = json.dumps(grupos_edades)

    return render(request, 'report.html', {'rangos_edades': rangos_edades_json})

from django.urls import path
from .views import list_task, create_task, delete_task, cont,editarTask

urlpatterns = [
    path('', list_task),
    path('new/', create_task),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('editarTask/<int:task_id>/', editarTask, name='editarTask'),

    path('cont/', cont),
    path('report/', cont, name='report_page'),  # Agregar esta línea para la página de informes
    

]

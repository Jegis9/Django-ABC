from django.urls import path
from .views import list_task, create_task, delete_task,edit_task,report
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', list_task, name='list_task'),
    path('new/', create_task),
    path('task/edit_task/<int:task_id>/', edit_task, name='edit_task'),

    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
   
    path('report/', report, name='report_page'),  # Agregar esta línea para la página de informes
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

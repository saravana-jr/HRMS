from django.contrib import admin
from django.urls import include, path
from peopleconnect.views import Leave,new_form,edit,view,delete

urlpatterns = [
    path('', Leave, name='Leave'),
    path('new/', new_form, name='new'),
    path('edit/<int:leave_id>/', edit, name='edit'),
    path('view/<int:leave_id>/', view, name='view'),
    path('delete/<int:leave_id>/', delete, name='delete'),
    path('admin/', admin.site.urls),
]
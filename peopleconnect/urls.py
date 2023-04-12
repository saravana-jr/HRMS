from django.contrib import admin
from django.urls import include, path
from peopleconnect.views import design,leave_submitted

urlpatterns = [
    path('design/', design, name='design'),
    path('sent/', leave_submitted, name='sent'),
    path('admin/', admin.site.urls),
]
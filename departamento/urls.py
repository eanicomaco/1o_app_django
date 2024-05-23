from django.urls import path
from departamento.views import departamentos

urlpatterns = [
    path('', departamentos, name='departamento.departamentos')
]
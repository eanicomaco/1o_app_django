from django.urls import path
from empresa.views import empresas

urlpatterns = [
    path('', empresas, name='empresa.empresas')
]
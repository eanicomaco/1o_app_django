from django.shortcuts import render

def departamentos(request):
    return render(request, 'departamento/departamentos.html')

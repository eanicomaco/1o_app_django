from django.shortcuts import render

def empresas(request):
    return render(request, 'empresa/empresas.html')

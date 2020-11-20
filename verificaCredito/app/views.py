from django.shortcuts import render

# Create your views here.
def buscar_empresas(request):
    empresa = "banco do brasil"
    return render(request, 'empresas/buscar_empresas.html', {"empresa": empresa})
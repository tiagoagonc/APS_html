from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app_aps/home.html', context={
        'name': 'Tiago Gonçalves',
    })


def contato(request):
    return render(request, 'app_aps/contato.html')


def sobre(request):
    return HttpResponse('SOBRE - Teste APS')

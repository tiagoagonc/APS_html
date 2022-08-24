from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app_aps/home.html', context={
        'name': 'Tiago Gonçalves',
    })


def contato(request):
    return HttpResponse('''
    <!DOCTYPE>
    <html>
    <head>
        <title>CONTATO - Teste APS</title>
    </head>
    <body>
        <h1>APS - Unimed Litoral</h1>
        <p>Contato</p>
    </body>
    </html>
    ''')


def sobre(request):
    return HttpResponse('SOBRE - Teste APS')

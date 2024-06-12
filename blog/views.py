from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicial(request):
    return HttpResponse("inicial")

def primera_vista(request):
    return HttpResponse("Hola :D")

def segunda_vista(request):
    respuesta = '''
        <h1>Hola a todos</h1>
        <p>Bienvenidos a mi sitio web</p>
        <a href="https://www.google.cl">Ir a Google</a>    
    '''
    return HttpResponse(respuesta)

def tercera_vista(request):
    return render(request, 'portafolio.html')
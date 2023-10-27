from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Articolo, Giornalista
""" def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a += (art.titolo +"<br>")
    for gio in Giornalista.objects.all():
        a += (gio.titolo +"<br>")
    responde= "articoli:<br>" + "<br>giornalisti:<br>" + g

    return HttpResponse("<h1>homepage news!</h1>") """

def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response= str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>"+response+"</h1>") 

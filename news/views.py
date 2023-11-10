from django.shortcuts import render, get_object_or_404
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

""" def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response= str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>"+response+"</h1>") """ 

def home(request):
        articoli = Articolo.objects.all()
        giornalisti = Giornalista.objects.all()
        context = {"articoli": articoli, "giornalisti": giornalisti}
        print(context)
        return render(request, "homepage1.html", context)

def articoloDetailView(request, pk):
        articolo = get_object_or_404(Articolo, pk=pk)
        context = {"articolo": articolo}
        return render(request, "articolo_detail.html", context)
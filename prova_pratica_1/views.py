from random import randint
from django.shortcuts import render

# Create your views here.

def index_prova(request):
    return render(request, "index_prova.html")

def maxmin(request):
    var1=randint(1,10)
    var2=randint(1,10)
    context={
        'var1':var1,
        'var2':var2,
        'var3':var1+var2
    }
    return render(request, "maxmin.html", context)

def media(request):
    array = []
    t=0
    for i in range (30):
        array.append(randint(1,10))
        t+=array[i]
    context={
        'array': array,
        'media': t/30
    }
    return render(request, "media.html", context)

def voti(request):
    context={
        'dizionario' : {'stud1':9,'stud2':5,'stud3':6,}        
    }
    return render(request, "voti.html", context)
from datetime import datetime
from multiprocessing import context
from django.shortcuts import render
import datetime

def indexVoti(request):
    return render (request, "indexVoti.html")

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={
        'materia':materie
    }
    return render (request, "materie.html", context)

def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    context={
        'diz':voti
    }
    return render (request, "dizionario.html", context)

def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

    media=0
    for key, values in voti.items():
        for x in values:
            for i in range(5):
                media+=voti[key][i][1]
            media/=5
    
    val=[(voti['Giuseppe Gullo'], media),(voti['Antonio Barbera'], media),(voti['Nicola Spina'], media)]
    context={
        'diz':voti,
        'medie':media
    }
    return render(request, "media.html", context)


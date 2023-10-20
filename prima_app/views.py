from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def welcome(request):
    return render(request,"welcome.html")
def lista(request):
    return render(request,"lista.html")
def chisiamo(request):
    return render(request,"chisiamo.html")
def variabili(request):
    context={
        'var1': 100,
        'var2': 200,
        'var3': 300
    }
    return render(request,"variabili.html",context)
def index(request):
    
    return render(request,"index.html")
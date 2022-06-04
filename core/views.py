from asyncio.log import logger
from cmath import log
from msilib.schema import ListView
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from core.form import *
from .models import *


#def welcome(request):
#    return HttpResponse("vien venido a esta pagina")
def index(request):
    return render(request,"index.html")

def login(request):
    #form = UserRegisterForm()
    UserAcces = {'form' : PostForm}
    return render(request,"login.html",UserAcces) 

def registro(request):
    if request.method=='POST':
        print(request.POST)
        #PostForm.save()
        form = PostForm(request.POST)
        if form.is_valid():
            print("Valido")
            form.save()
        else:
            print("Invalido")    
        personas = Usuario.objects.distinct()

        return render(request,"consulta.html",{ 'personas':personas })   
    else:    
        UserAcces = {'form' : PostForm}
        return render(request,"registro.html",UserAcces)        


def puestoPersonas(request):    
    print("hola")
    personas = Usuario.objects.distinct()
    print(personas)
    return render(request,'consulta.html',{ 'personas':personas })
    

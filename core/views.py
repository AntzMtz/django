from django.http import HttpResponse
from django.shortcuts import render
#def welcome(request):
#    return HttpResponse("vien venido a esta pagina")
def welcome(request):
    return render(request,"welcome.html")
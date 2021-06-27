from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Pratik','place':'India'}
    return render(request,'index.html',params)

def removepunc(request):
    return HttpResponse("<h1>Remove punc</h1>")

def capitalizefirst(request):
    return HttpResponse("<h1>capitalize first</h1>")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremover(request):
    return HttpResponse("spaceremover<a href=''>Back</a>")

def charcount(request):
    return HttpResponse("charcount")
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    #Get the text
    djtext=request.GET.get('text', 'default')
    print(djtext)
    #analyze the text
    return HttpResponse("<h1>Remove punc</h1>")

def capitalizefirst(request):
    return HttpResponse("<h1>capitalize first</h1>")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremover(request):
    return HttpResponse("spaceremover<a href=''>Back</a>")

def charcount(request):
    return HttpResponse("charcount")
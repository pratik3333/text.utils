from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext=request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        # analyzed= djtext
        punctuation = '''?<>~"':;,//\|[]{}_.!@#$%^&*()-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Uppercae', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
#
# def capitalizefirst(request):
#     return HttpResponse("<h1>capitalize first</h1>")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremover(request):
#     return HttpResponse("spaceremover<a href=''>Back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount")
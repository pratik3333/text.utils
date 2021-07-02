from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text', 'default')
    #check checkbox values
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuation = '''?<>~"':;,//\|[]{}_.!@#$%^&*()-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'changed to Uppercae', 'analyzed_text': analyzed}
        # analyze the text
        #return render(request, 'analyze.html', params)
        djtext=analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        #analyze the text
        #return render(request, 'analyze.html', params)
        djtext=analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        # analyze the text
        #return render(request, 'analyze.html', params)
        djtext=analyzed


    return render(request, 'analyze.html', params)





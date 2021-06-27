# I have created this file -pratik

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''<h1>Pratik</h1> <a href="https://www.youtube.com/watch?v=Uh2ebFW8OYM"> 1.Python CoreySchafer:-</a>''')

def fort(request):
    s='''<marquee direction = "right"><h1>Forts<br></h1></marquee>
    <center><a href="https://en.wikipedia.org/wiki/Raigad_Fort">1.Raigad - click here for information about Raigad:-</a></center><br>
    <center><a href="https://en.wikipedia.org/wiki/Rajgad_Fort">2.Rajgad - click here for information about Rajgad:-</a></center><br>
    <center><a href="https://en.wikipedia.org/wiki/Torna_Fort"> 3.Torna - click here for information about Torna:-</a></center><br>'''
    return HttpResponse(s)

def abc(request):
    params={'name':'kunal','place':'Maharashtra'}
    return render(request,'abc.html',params)


def about(request):
    return HttpResponse("Hello about")
# I have created this file -pratik

from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Pratik</h1> <a href="https://www.youtube.com/watch?v=Uh2ebFW8OYM"> 1.Python CoreySchafer:-</a>''')

def rajgad(request):
    return HttpResponse('''<h1>Rajgad</h1> <a href="https://en.wikipedia.org/wiki/Rajgad_Fort"> 2.Rajgad information about rajgad:</a>''')


def about(request):
    return HttpResponse("Hello about")
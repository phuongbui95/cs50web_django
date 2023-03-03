from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world!")
    
    ### Add the entire website to request
    return render(request, "hello/index.html")

def pb(request):
    return HttpResponse("Hello, Pb!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
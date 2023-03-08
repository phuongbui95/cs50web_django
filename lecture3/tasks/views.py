from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context)

def add(request):
    return render(request, "tasks/add.html")

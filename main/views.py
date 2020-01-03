from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreatNewList

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    #return HttpResponse("<h2>Welcome to default %s page</h2>" %ls.name)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == 'POST':
        form = CreatNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreatNewList()
    return render(response, "main/create.html", {"form":form})

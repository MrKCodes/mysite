from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h2>Welcome to default %s page</h2>" %ls.name)


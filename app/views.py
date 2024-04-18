from django.shortcuts import render
from .models import Person
# Create your views here.

def home(request):
    return render(request, "home.html")


def listPersons(request):
    persons = Person.objects.all()
    return render(request, "persons.html", {"persons": persons})


def showPerson(request, id):
    person = Person.objects.get(pk=id)   
    return render(request, "person.html", {"person": person})
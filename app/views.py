from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
# Create your views here.

def home(request):
    return render(request, "home.html")


def listPersons(request):
    persons = Person.objects.all()
    return render(request, "persons.html", {"persons": persons})


def showPerson(request, id):
    person = Person.objects.get(pk=id)   
    return render(request, "person.html", {"person": person})

def createPerson(request):
    
    if request.method == "GET":
        form = PersonForm()  
        return render(request,"createPerson.html",{'form':form})  
    
    elif request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
        
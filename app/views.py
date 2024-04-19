from django.shortcuts import render,redirect,get_object_or_404
from .models import Person
from .forms import PersonForm
# Create your views here.

def home(request):
    return render(request, "home.html")


def listPersons(request):
    persons = Person.objects.all()
    return render(request, "persons.html", {"persons": persons})


def showPerson(request, id):
    person = get_object_or_404(Person,pk=id)   
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
    

def updatePerson(request,id):

    person = get_object_or_404(Person,pk=id) 
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("person",id)
    else:
        form = PersonForm( instance=person)
    return render(request,'update.html', {'form': form,'person':person})
     

def deletePerson(request,id):
    if request.method == "GET":
        person = get_object_or_404(Person,pk=id) 
        person.delete()
        return redirect("persons")
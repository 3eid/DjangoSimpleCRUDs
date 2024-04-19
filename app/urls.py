from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.home, name='home'),
    path('persons', views.listPersons, name='persons'),
    path('persons/<int:id>', views.showPerson, name='person'),
    path('persons/create', views.createPerson, name='createPerson'),
    path('persons/update/<int:id>', views.updatePerson, name='updatePerson'),
    path('persons/delete/<int:id>', views.deletePerson, name='deletePerson'),

]

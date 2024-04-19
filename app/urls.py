from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.home, name='home'),
    path('persons', views.listPersons, name='persons'),
    path('persons/<int:id>', views.showPerson, name='person'),
    path('persons/create', views.createPerson, name='createPerson'),
    path('persons/<int:id>/update', views.updatePerson, name='updatePerson'),
    path('persons/<int:id>/delete', views.deletePerson, name='deletePerson'),

]

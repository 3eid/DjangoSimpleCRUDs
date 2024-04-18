from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.home, name='home'),
    path('persons', views.listPersons, name='persons'),
    path('person/<int:id>', views.showPerson, name='person'),
]

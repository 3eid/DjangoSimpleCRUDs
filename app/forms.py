from django.forms import ModelForm,DateInput
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["id", "name", "age", "nationalityID","birthDate"]
        widgets = {
                'birthDate': DateInput(attrs={'type': 'date'}),
            }
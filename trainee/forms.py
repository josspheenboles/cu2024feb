from django import forms
from .models import *
from django.core.exceptions import ValidationError
class TraineeForm(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField()
    img = forms.ImageField()
    def clean_name(self):
        obj=Trainee.objects.get(name=self.cleaned_data['name']).exsists()
        if obj:
            raise ValidationError("Name Must Be unique")

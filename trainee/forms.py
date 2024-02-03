from django import forms
from .models import *
from track.models import *
from django.core.exceptions import ValidationError
class TraineeForm(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField()
    img = forms.ImageField()
    track=forms.ChoiceField(choices=Track.get_all_tracks())
    # def clean_name(self):
    #     print(self.cleaned_data)
    #     obj=Trainee.objects.filter(name=self.cleaned_data['name']).exsists()
    #     if obj:
    #        raise ValidationError("Name Must Be unique")
    #     return True

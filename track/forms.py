from django import forms
from .models import *
class Trackform(forms.ModelForm):
    model=Track
    fields='__all__'
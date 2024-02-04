from django import forms
from .models import *
class Trackform(forms.ModelForm):
    class Meta:
        model=Track
        fields='__all__'

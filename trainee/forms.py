from django import forms
class TraineeForm(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField()
    img = forms.ImageField()

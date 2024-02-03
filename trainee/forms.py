from django import forms
class TraineeForm(forms.Form):
    name = forms.CharField(required=True,unique=True)
    age = forms.IntegerField(required=True,default=21)
    email = forms.EmailField()
    img = forms.ImageField(upload_to='trainee/images', blank=True, null=True)

from django.shortcuts import render
from .models import *
# Create your views here.
def traineelist(request):
    trainees=Trainee.objects.all()
    context={'trainess':trainees}
    return  render(request,'trainee/index.html',context)
def traineedetails(request,id):
    trainee = Trainee.objects.get(id=id)
    context = {'trainee': trainee}
    return render(request, 'trainee/traineedetails.html', context)
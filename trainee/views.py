from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.
def traineelist(request):
    #trainees=Trainee.objects.all()
    #context={'trainess':trainees}
    #more readable
    context={'trainess':Trainee.get_all_trainees()}
    return  render(request,'trainee/index.html',context)
def traineedetails(request,id):
    trainee = Trainee.objects.get(id=id)
    context = {'trainee': trainee}
    return render(request, 'trainee/traineedetails.html', context)
def traineeDelete(request,id):
    trainee = Trainee.objects.get(id=id).delete()

    return HttpResponseRedirect(reverse('trainee.list'))
def traineeupdate(request,id):
    context = {}
    if(request.method=='POST'):
        trainee = Trainee.objects.get(id=id)
        trainee.name=request.POST['name']
        trainee.email=request.POST['email']
        trainee.save()
        return HttpResponseRedirect(reverse('trainee.list'))
    trainee = Trainee.objects.get(id=id)
    context['trainee']=trainee
    return render(request, 'trainee/traineeupdate.html', context)
def traineeadd(request):
    context = {}
    if(request.method=='POST'):
        trainee = Trainee()
        trainee.name=request.POST['name']
        trainee.email=request.POST['email']
        trainee.img=request.FILES['image']
        trainee.save()
        return HttpResponseRedirect(reverse('trainee.list'))

    return render(request, 'trainee/traineeadd.html')
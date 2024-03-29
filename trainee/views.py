from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.
from django.views import View
from django.contrib.auth.decorators import login_required
class traineeupdateClass(View):
    def get(self,request,id):
        context={}
        trainee = Trainee.objects.get(id=id)
        form=Traineeaddmodel( instance=trainee)
        context['form'] = form
        return render(request, 'trainee/traineeupdateclass.html', context)
    def post(self,request,id):
        form = Traineeaddmodel(request.POST,request.FILES)
        if(form.is_valid()):
            trainee=form.save()
            return HttpResponseRedirect(reverse('trainee.list'))

def traineelist(request):
    #trainees=Trainee.objects.all()
    #context={'trainess':trainees}
    #more readable
    context={'trainess':Trainee.get_all_trainees()}
    return  render(request,'trainee/index.html',context)
def traineedetails(request,id):
    #trainee = Trainee.objects.get(id=id)
    #context = {'trainee': trainee}
    context = {'trainee': Trainee.get_trainee_by_id(id)}
    return render(request, 'trainee/traineedetails.html', context)
@login_required()
def traineeDelete(request,id):
    trainee = Trainee.objects.get(id=id).delete()

    return HttpResponseRedirect(reverse('trainee.list'))
@login_required()
def traineeupdate(request,id):
    context = {}
    if(request.method=='POST'):
        trainee = Trainee.objects.get(id=id)
        trainee.name=request.POST['name']
        trainee.email=request.POST['email']
        trainee.track=Track.objects.get(id=request.POST['track'])
        trainee.save()
        return HttpResponseRedirect(reverse('trainee.list'))
    trainee = Trainee.objects.get(id=id)
    tracks = Track.get_all_tracks()
    context['trainee']=trainee
    context['tracks']=tracks
    return render(request, 'trainee/traineeupdate.html', context)
@login_required()
def traineeadd(request):
    context = {}
    if(request.method=='POST'):
        trainee = Trainee()
        trainee.name=request.POST['name']
        trainee.email=request.POST['email']
        trainee.img=request.FILES['image']

       # trainee.track=Track.objects.get(id=request.POST['track'])
        trainee.save()
        return HttpResponseRedirect(reverse('trainee.list'))

    return render(request, 'trainee/traineeadd.html')

@login_required()
def traineeaddForm(request):
    context = {'form':TraineeForm()}
    if(request.method=='POST'):
        form=TraineeForm(request,request.POST,request.FILES)
        # if(form.is_valid()):
        trainee = Trainee()
        trainee.name=request.POST['name']
        trainee.email=request.POST['email']
        trainee.img=request.FILES['img']
        print(request.POST['track'])
        trainee.track=Track.objects.get(id=request.POST['track'])
        trainee.save()
        print(request.POST)
        return HttpResponseRedirect(reverse('trainee.list'))

    return render(request, 'trainee/traineeaddForm.html',context)

@login_required()
def traineeaddFormModel(request):
    context={'form':Traineeaddmodel()}
    if(request.method=='POST'):
        form=Traineeaddmodel(request.POST,request.FILES)
        if(form.is_valid()):
            traineeobj=form.save()
            return HttpResponseRedirect(reverse('trainee.details',args=[traineeobj.id]))
    return render(request,'trainee/traineeaddFormModel.html',context)
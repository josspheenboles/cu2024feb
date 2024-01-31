from django.shortcuts import render

# Create your views here.
def traineelist(request):
    return  render(request,'trainee/index.html')
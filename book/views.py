from django.shortcuts import render

# Create your views here.
def List(request):
    return  render(request,'book/index.html')
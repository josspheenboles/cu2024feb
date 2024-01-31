from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<center><h1 style='color:red'>hello cairo uni. developers</h1></center>")

def getauthorbyname(request,authorname):
    return HttpResponse(f"<h1>Author:<span style='color:green'>{authorname}</span></h1>")
def getauthorbyid(request,id):
    return HttpResponse(f"<h1>Author:<span style='color:green'>{id}</span></h1>")

def promotcalculation(request,salary):
    print(salary)
    newsalary=float(salary)*10/100
    return HttpResponse(f"<h1>Author Salary:<span style='color:green'>{newsalary}</span></h1>")

data=[
{'id':1,'name':'aya','path':'1.webp'},
{'id':2,'name':'mark','path':'2.webp'},
{'id':3,'name':'ali','path':'3.webp'},
{'id':4,'name':'sara','path':'4.webp'},
]

def listall(request):
    context={'authors':data}
    return  render(request,"author/index.html",context)
    #return HttpResponse(data)
def listauthor(request,id):

    author=filter(lambda u:u['id']==id,data)
    #print(list(author)[0])
    l=list(author)[0]
    print(l)
    if 'id' in l:
        print('in')
        return HttpResponse(l.values())
    return HttpResponse("Id Not found")
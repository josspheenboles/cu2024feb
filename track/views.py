from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
#httprequest,return httpresponse
tracks=[
    {'id':1,'Name':'os','path':'os.png'},
    {'id':2,'Name':'IOT','path':'iot.png'},
    {'id':3,'Name':'Python','path':'python.jpeg'},
    {'id':4,'Name':'php','path':'php.png'},
]
def hellcu(request):
    return  HttpResponse('<h1>welcome to django <span style="color:green">cu</span> developers</h1>')
def tracklist(request):
    #return HttpResponse('<h1>Tracks list</h1>')
    #return HttpResponse(tracks)
    context={}
    context['tracks']=tracks
    return  render(request,'track/index.html',context)
def trackdetails(request,trackid):
    #print(type(trackid))
    #print((trackid)+10)
    #map,filter
    #lambda  input:output
    track=filter(lambda t:t['id']==trackid,tracks)
    #return HttpResponse(f'<h1>Track info</h1></br>Track id :{trackid}')
    track=list(track)
    if track:
        return HttpResponse(track)
    return HttpResponse('<span style="color:red">track not found</span>')

from django import views
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from trainee.models import *
def hell(request):
    return JsonResponse({"id":1,"name":"ali"})
@api_view(['GET'])
def hellapi(request):
    return Response({"id":1,"name":"ali"})

@api_view(['GET',"POST"])
def accept_data(request):
    if(request.method=='POST'):
        return Response(
            {"data":request.data,"msg":"request recived"},
            status=200)
    return Response({"data":"get request received"})

@api_view(['GET'])
def getall(request):
    trainees=Trainee.get_all_trainees()
    #serlizer manull
    selizeddata={"id":trainees[0].id,"name":trainees[0].name}
    return Response({"msg":"done","data":selizeddata})
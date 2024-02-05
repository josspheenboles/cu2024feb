from django import views
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from trainee.models import *
from .serlizer import *


@api_view(['GET'])
def getbyid(request,id):
    traineedata=Trainee.objects.filter(id=id)
    if(len(traineedata)>0):
        return Response(data={'data':Traineeserlizer(traineedata[0]).data   },status=200)
    return Response({'msg':'trainee not found'},status=200)
@api_view(['DELETE'])
def deletebyid(request,id):
    traineedata=Trainee.objects.filter(id=id)
    if(len(traineedata)>0):
        traineedata.delete()
        return Response(data={'msg':'deleted'})
    return Response({'msg':'trainee not found'})

@api_view(['GET','PUT'])
def updatebyid(request,id):
    traineedata = Trainee.objects.filter(id=id).first()

    if(traineedata):
        serlizeddata=Traineeserlizer(instance=traineedata,data=request.data)
        if serlizeddata.is_valid():
            serlizeddata.save()
            return Response(data=serlizeddata.data,status=200)
    return Response(serlizeddata.errors,status=400)

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
    selizeddata=[]
    for trainee in trainees:
        selizeddata.append(Traineeserlizer(trainee).data)

    return Response({"msg":"done","data":selizeddata})
    # return Response({"msg":"done","data":Traineeserlizer(trainees,many=True)})

@api_view(['POST'])
def add(request):
    # trainee=Trainee()
    # trainee.name=request.data['name']
    # trainee.createdat=request.data['createdat']
    # trainee.save()
    # Trainee.objects.create(**request.data)
    trainee=Traineeserlizer(data=request.data)
    if(trainee.is_valid()):
        trainee.save()
        return  Response({'msg':'trainee added'})
    return Response(trainee.errors,status=400)
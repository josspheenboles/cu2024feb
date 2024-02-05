from django import views
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import  Response

def hellapi(request):
    return JsonResponse({"id":1,"name":"ali"})
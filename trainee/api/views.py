from django import views
from django.http import JsonResponse
def hellapi(request):
    return JsonResponse('{"id":1,"name":"ali"}')
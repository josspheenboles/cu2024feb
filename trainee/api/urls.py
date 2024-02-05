from django.urls import path
from .views import *
urlpatterns=[
    path('Hello/',hell),
    path('HelloAPI/',hellapi),
    path('acceptdata/',accept_data),
    path('all/',getall),
    path('add/',add),
    path('getbyid/<id>',getbyid),
    path('deletebyid/<id>',deletebyid),
    path('update/<id>',updatebyid),
]
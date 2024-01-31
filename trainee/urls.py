from django.urls import path
from . import  views
urlpatterns=[
    path('List',views.traineelist),
    path('<int:id>',views.traineedetails,name="trainee.details"),
]
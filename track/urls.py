from django.urls import path
from . import  views
urlpatterns = [
    path('List',views.TrackList.as_view()),
    path('<int:pk>',views.TrackDetails.as_view(),name="track.details"),

]

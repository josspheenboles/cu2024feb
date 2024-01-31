from django.urls import path
from . import  views
urlpatterns = [
    path('List',views.tracklist),
    path('<int:trackid>',views.trackdetails,name="track.details"),

]

from django.urls import path
from . import  views
urlpatterns = [
    path('List',views.TrackList.as_view()),
    # path('<int:trackid>',views.trackdetails,name="track.details"),

]

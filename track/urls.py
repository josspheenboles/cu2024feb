from django.urls import path
from . import  views
urlpatterns = [
    path('List',views.TrackList.as_view(),name='track.list'),
    path('<int:pk>',views.TrackDetails.as_view(),name="track.details"),
    path('update/<int:pk>',views.TrackUpdate.as_view(),name="track.Update"),

]

from django.urls import path
from . import  views
urlpatterns = [
    path('List',views.TrackList.as_view(),name='track.list'),
    path('Create',views.TrackCreate.as_view(),name='track.create'),
    path('<int:pk>',views.TrackDetails.as_view(),name="track.details"),
    path('update/<int:pk>',views.TrackUpdate.as_view(),name="track.Update"),
    path('delete/<int:pk>',views.Trackdelete.as_view(),name="track.delete"),

]

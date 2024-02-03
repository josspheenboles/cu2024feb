from django.urls import path
from . import  views
urlpatterns=[
    path('List',views.traineelist,name="trainee.list"),
    path('add',views.traineeadd,name="trainee.add"),
    path('addForm',views.traineeaddForm,name="trainee.addForm"),
    path('<int:id>',views.traineedetails,name="trainee.details"),
    path('Update/<int:id>',views.traineeupdate,name="trainee.update"),
    path('Delete/<int:id>',views.traineeDelete,name="trainee.Delete"),
]
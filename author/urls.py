from django.urls import path,re_path
from .views import *
urlpatterns=[


    re_path(r'Promot/(?P<salary>[-+]?\d*\.\d+|\d+)$', promotcalculation, name='promote_author'),
    # path('Author/Promot/<int:salary>',views.promotcalculation),
    path('<int:id>', getauthorbyid),
    path('ListAll/', listall),
    path('List/<int:id>', listauthor,name='author.id'),
    #path('<authorname>', getauthorbyname),
]
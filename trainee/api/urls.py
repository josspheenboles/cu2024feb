from django.urls import path
from .views import *
urlpatterns=[
    path('Hello/',hell),
    path('HelloAPI/',hellapi),
    path('acceptdata/',accept_data),
]
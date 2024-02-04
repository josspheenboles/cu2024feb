from django.shortcuts import reverse,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
def profile(request):
    return redirect(reverse('track.list'))

class Registratoin(CreateView):
    model = User
    template_name = 'registration/Registratoin.html'
    form_class =UserCreationForm
    success_url = reverse_lazy('track.list')
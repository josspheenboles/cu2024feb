from django.shortcuts import reverse,redirect
def profile(request):
    return redirect(reverse('track.list'))
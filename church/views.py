from django.shortcuts import render
from .models import Department, Family, Announcement, Member, Event
from django.utils.translation import gettext_lazy as _

# Create your views here.

def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'home.html', context)
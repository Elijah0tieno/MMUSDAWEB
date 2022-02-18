from django.shortcuts import render
from .models import Department, Family, Announcement, Member, Event
# Create your views here.

def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'home.html', context)
from django.shortcuts import render
from .models import Department, Family, Announcement, Member, CalendaOfEvents
# Create your views here.

def home(request):
    context = {
        'events': CalendaOfEvents.objects.all()
    }
    return render(request, 'home.html', context)
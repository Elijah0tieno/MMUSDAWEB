from django.shortcuts import render
from .models import Department, Family, Announcement, Member, Event
# from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your views here.

def home(request):
    today = datetime.today()

    events = Event.objects.order_by('start_date').all()
    latest_events =  Event.objects.filter(start_date__lte=today, end_date__gte=today).order_by('start_date').all()

    context = {
        'events': events,
        'latest_events': latest_events,
    }
    print(events[3].poster)
    return render(request, 'home.html', context)
    

def department(request):
    context = {
        'departments': Department.objects.all()
    }
    return render(request, 'departments.html', context=context)

def family(request):
    context = {
        'families': Family.objects.all()
    }
    return render(request, 'families.html', context=context)

def announcement(request):
    context = {
        'announcements': Announcement.objects.all()
    }
    return render(request, 'announcements.html', context=context)

def event(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events.html', context=context)

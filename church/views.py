from django.shortcuts import render
from .models import Department, Family, Announcement, Member, Event
from django.utils.translation import gettext_lazy as _

# Create your views here.

def home(request):
    context = {
        'events': Event.objects.all()
    }
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
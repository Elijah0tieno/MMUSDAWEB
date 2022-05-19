from django.urls import path
from .views import home
from . import views

app_name = 'church'

urlpatterns = [
    path('', home, name='home'),
    path('departments/', views.department, name='departments'),
    path('families/',views.family, name='families'),
    path('announcements/', views.announcement, name='announcements'),
    path('events/', views.event, name='events'),
]
from django.urls import path
from .views import home

app_name = 'church'

urlpatterns = [
    path('', home, name='home')
]
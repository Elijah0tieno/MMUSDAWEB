from django.urls import path
from .views import home
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'church'

urlpatterns = [
    path('', home, name='home'),
    path('departments/', views.department, name='departments'),
    path('families/',views.family, name='families'),
    path('announcements/', views.announcement, name='announcements'),
    path('events/', views.event, name='events'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from .models import Department, Family, Announcement, Member

# Register your models here.
admin.site.register(Department)
admin.site.register(Family)
admin.site.register(Announcement)
admin.site.register(Member)
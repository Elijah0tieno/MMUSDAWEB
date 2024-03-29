from django.db import models
from django.core.files.storage import FileSystemStorage
from sorl.thumbnail import ImageField
from mmusdaweb.storages import PublicMediaStorage, PrivateMediaStorage
# fs = FileSystemStorage(location='/media/photos')

def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)

# media/posts/user_id/filename

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=250)
    head = models.CharField(max_length=250)
    assistant = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    event_name = models.CharField(max_length=250)
    poster = ImageField(upload_to='images/')
    # week = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.event_name
    
    
class Family(models.Model):
    name = models.CharField(max_length=250)
    history = models.CharField(max_length=250)
    dad = models.CharField(max_length=250)
    mum = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Announcement(models.Model):
    item = models.TextField()
    date = models.DateField()

    
    def __str__(self):
        return self.item
    
class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=250)
    head = models.CharField(max_length=250)
    assistant = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=250)
    history = models.CharField(max_length=250)
    dad = models.CharField(max_length=250)
    mum = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Announcement(models.Model):
    item = models.CharField(max_length=1500)
    date = models.DateField()
    
    def __str__(self):
        return self.item
    
class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.RESTRICT)
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
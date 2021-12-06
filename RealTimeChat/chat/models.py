from django.db import models
import sys
from datetime import datetime

from django.db.models.deletion import CASCADE
# Create your models here.
class room(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class message(models.Model):
    value = models.CharField(max_length=sys.maxsize)
    date = models.DateField(default=datetime.now,blank=True)
    room = models.IntegerField(blank=True,null=True)
    user = models.CharField(max_length=30,null=True)
    def __str__(self) -> str:
        return self.user
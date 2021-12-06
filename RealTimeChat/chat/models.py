from django.db import models
import sys
from datetime import datetime

from django.db.models.deletion import CASCADE
# Create your models here.
class room(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=50)

class message(models.Model):
    value = models.CharField(max_length=sys.maxsize)
    date = models.DateField(default=datetime.now,blank=True)
    room = models.ForeignKey(room,blank=True, null=True, on_delete=models.SET_NULL)
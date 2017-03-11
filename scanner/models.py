from django.db import models
import datetime

# Create your models here.

current_time = datetime.datetime.now()

class Scan(models.Model):

    name = models.TextField(null=False, blank=False)
    created = models.DateTimeField(null=False, blank=False, default=current_time)
    last_run = models.DateTimeField(null=False, blank=False, default=current_time)


class Ip(models.Model):

    ip = models.TextField(null=False, blank=False)
    scan = models.ForeignKey(Scan, null=False)

class Port(models.Model):
   
    ip = models.ForeignKey(Ip, null=True, blank=True)
    scan = models.ForeignKey(Scan, null=False)
    number = models.IntegerField(null=False)
    active = models.IntegerField(null=False, default = 0)

from django.db import models
from datetime import datetime 

class DestinationCategory(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class AttractionCategory(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default="")
    location = models.CharField(max_length=30, default="")
    category = models.ForeignKey(DestinationCategory, default=1)
    description = models.CharField(max_length=200, default="")
    best_time = models.CharField(max_length=50, default="")
    open_hours = models.CharField(max_length=50, default="")
    time_required = models.CharField(max_length=50, default="")
    photos = models.CharField(max_length=50, default="")
    added_on = models.DateField(default="1/1/1")
    added_by = models.CharField(max_length=20, default="aju")

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        return self.name + ", " + self.state + ", " + self.country

class Attraction(models.Model):
   name = models.CharField(max_length=50)
   state = models.CharField(max_length=50)
   country = models.CharField(max_length=50)
   address = models.CharField(max_length=50)
   location = models.CharField(max_length=30)
   category = models.ForeignKey(AttractionCategory, default=1)
   description = models.CharField(max_length=200, default="")
   best_time = models.CharField(max_length=50, default="")
   open_hours = models.CharField(max_length=50, default="")
   ticket_price = models.CharField(max_length=50, default="")
   time_required = models.CharField(max_length=50, default="")
   photos = models.CharField(max_length=50, default="")
   added_on = models.DateTimeField('Date Added', default=datetime.now)
   added_by = models.CharField(max_length=20, default="aju")

   def __unicode__(self):
       return self.full_name()

   def full_name(self):
       return self.name + ", " + self.state + ", " + self.country


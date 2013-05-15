from django.db import models

# Create your models here.
class Chapter(models.Model):
  order = models.IntegerField()
  title = models.CharField(max_length=400)
  start_date = models.DateField()
  end_date = models.DateField()
  summary = models.TextField()
  
  def __unicode__(self):
    return self.title

class Event(models.Model):
  time = models.DateField()
  content = models.TextField()
  chapter = models.ForeignKey(Chapter)
  
  def __unicode__(self):
    return self.content
from django.db import models
from django.conf import settings

class Tag(models.Model):
  name = models.TextField()
  def __unicode__(self):
    return self.name

class Role(models.Model):
  name = models.TextField()
  def __unicode__(self):
    return self.name

class Project(models.Model):
  title = models.TextField()
  description = models.TextField()
  owner = models.TextField()
  owner_email = models.TextField()
  owner_role = models.TextField()
  tags = models.ManyToManyField(Tag)
  is_sponsored = models.BooleanField(default=False)
  is_completed = models.BooleanField(default=False)
  def __unicode__(self):
    return self.title

class Wanted(models.Model):
  project = models.ForeignKey(Project)
  role = models.ForeignKey(Role)
  description = models.TextField()

class Comment(models.Model):
  user = models.TextField()
  text = models.TextField()

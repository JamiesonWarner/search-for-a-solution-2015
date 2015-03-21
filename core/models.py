from django.db import models
from django.conf import settings

class Tag(models.Model):
  name = models.TextField()
  def __unicode__(self):
    return name

class Role(models.Model):
  name = models.TextField()
  def __unicode__(self):
    return name

class Student(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)

class Project(models.Model):
  title = models.TextField()
  description = models.TextField()
  owner = models.ForeignKey(Student)
  owner_role = models.ForeignKey(Role)
  tags = models.ManyToManyField(Tag)
  is_sponsored = models.BooleanField(default=False)
  is_completed = models.BooleanField(default=False)
  def __unicode__(self):
    return title

class Wanted(models.Model):
  project = models.ForeignKey(Project)
  role = models.ForeignKey(Role)
  description = models.TextField()

class Comment(models.Model):
  user = models.ForeignKey(Student)
  text = models.TextField()

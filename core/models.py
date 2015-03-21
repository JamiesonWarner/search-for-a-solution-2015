from django.db import models
from django.conf import settings

class Tag(models.Model):
  name = models.TextField()

class Student(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  tags = models.ManyToManyField(Tag)

class Project(models.Model):
  title = models.TextField()
  description = models.TextField()
  owner = models.ForeignKey(Student)
  is_sponsored = models.BooleanField(default=False)
  is_paid = models.BooleanField(default=False)
  is_completed = models.BooleanField(default=False)

class Wanted(models.Model):
  description = models.TextField()
  tags = models.ManyToManyField(Tag)
  project = models.ForeignKey(Project)

class Comment(models.Model):
  user = models.ForeignKey(Student)
  text = models.TextField()

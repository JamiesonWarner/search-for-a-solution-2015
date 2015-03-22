from django.forms import widgets
from rest_framework import serializers
from core.models import *

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag

class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role

class WantedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Wanted

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment


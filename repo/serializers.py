from rest_framework import serializers
from .models import Projects, LANGUAGE_CHOICES, STYLE_CHOICES,Profile
from django.contrib.auth.models import User


class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ('title','image','description','link','owner')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=('user','bio','projects','image')










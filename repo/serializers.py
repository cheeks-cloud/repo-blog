from rest_framework import serializers
from .models import Projects, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ('title','image','description','link','owner')


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,view_name='projects-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'projects','url','projects')










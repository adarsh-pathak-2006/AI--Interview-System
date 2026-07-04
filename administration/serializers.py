from rest_framework.serializers import ModelSerializer
from administration.models import Profile, Resume, Project
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class ProfileSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields='__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'


class ResumeSerializer(ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    projects=ProjectSerializer(read_only=True, many=True)
    class Meta:
        model=Resume
        fields='__all__'



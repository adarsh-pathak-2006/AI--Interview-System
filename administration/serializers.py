from rest_framework.serializers import ModelSerializer
from administration.models import Profile, Resume, Project

class Profile(ModelSerializer):
    class Meta:
        model=Profile
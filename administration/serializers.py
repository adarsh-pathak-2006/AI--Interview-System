from rest_framework.serializers import ModelSerializer
from administration.models import Profile, Resume, Project
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['resume']


class ResumeSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    projects = ProjectSerializer(read_only=True, many=True)
    class Meta:
        model = Resume
        fields = '__all__'

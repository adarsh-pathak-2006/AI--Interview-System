from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from administration.models import Profile, Resume, Project
from administration.serializers import UserSerializer, ProfileSerializer, ProjectSerializer, ResumeSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class RegisterAPI(CreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()


class ResumeAPI(ListCreateAPIView):
    serializer_class=ResumeSerializer

    def get_queryset(self):
        profile_object=get_object_or_404(Profile, user=self.request.user)
        return Resume.objects.filter(profile=profile_object)
    
    def perform_create(self, serializer):
        data=get_object_or_404(Profile, user=self.request.user)
        serializer.save(profile=data)
    
class ResumeAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=ResumeSerializer

    def get_queryset(self):
        profile_object=Profile.objects.filter(user=self.request.user)
        return Resume.objects.filter(profile=profile_object)

class ProjectAPI(ListCreateAPIView):
    serializer_class=ProjectSerializer

    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        resume_data=Resume.objects.filter(profile=profile_data)
        return Project.objects.filter(corresponding_resume=resume_data)
    
    def perform_create(self, serializer):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        resume_data=Resume.objects.filter(profile=profile_data)
        serializer.save(corresponding_resume=resume_data)

class ProjectAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectSerializer

    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        resume_data=Resume.objects.filter(profile=profile_data)
        return Project.objects.filter(corresponding_resume=resume_data)
    

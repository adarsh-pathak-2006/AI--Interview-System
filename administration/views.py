from django.shortcuts import render
from django.contrib.auth.models import User
from administration.models import Profile, Resume, Project
from administration.serializers import UserSerializer, ProfileSerializer, ProjectSerializer, ResumeSerializer
from rest_framework.generics import CreateAPIView


class RegisterAPI(CreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()



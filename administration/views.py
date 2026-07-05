from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from administration.models import Profile, Resume, Project
from administration.serializers import UserSerializer, ProfileSerializer, ProjectSerializer, ResumeSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegisterAPI(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Profile.objects.create(user=user, full_name=user.first_name + " " + user.last_name)


class ResumeAPI(ListCreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(profile__user=self.request.user)
    
    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer.save(profile=profile)
    

class ResumeAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(profile__user=self.request.user)


class ProjectAPI(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        resume_id = self.request.query_params.get('resume_id')
        qs = Project.objects.filter(resume__profile__user=self.request.user)
        if resume_id:
            qs = qs.filter(resume_id=resume_id)
        return qs
    
    def perform_create(self, serializer):
        resume_id = self.request.data.get('resume_id')
        resume = get_object_or_404(Resume, id=resume_id, profile__user=self.request.user)
        serializer.save(resume=resume)


class ProjectAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(resume__profile__user=self.request.user)

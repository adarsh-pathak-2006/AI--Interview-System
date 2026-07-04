from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=150)
    github=models.URLField()
    linkedin=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
    
class Resume(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    summary=models.TextField()
    course=models.CharField(max_length=100)
    college=models.CharField(max_length=200)
    cgpa=models.FloatField()

    def __str__(self):
        return self.profile.full_name
    
class Project(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField()
    github=models.URLField()
    live_link=models.URLField(blank=True)
    corresponding_resume=models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name[:100]






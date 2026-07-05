from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=150)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Resume(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='resumes')
    summary = models.TextField()
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    cgpa = models.FloatField()

    def __str__(self):
        return f"Resume for {self.profile.full_name}"
    
class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=300)
    description = models.TextField()
    github = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.name[:100]

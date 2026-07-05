from django.db import models
from administration.models import Resume

class Interview(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='interviews')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview for {self.resume.profile.full_name} ({self.status})"

class Question(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return f"Q{self.order}: {self.text[:50]}"

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    user_answer = models.TextField()
    score = models.IntegerField(null=True, blank=True)
    ai_feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to {self.question.id}"

class Analysis(models.Model):
    interview = models.OneToOneField(Interview, on_delete=models.CASCADE, related_name='analysis')    
    scores = models.JSONField()
    strengths = models.JSONField()
    weaknesses = models.JSONField()
    missing_skills = models.JSONField()
    project_analysis = models.JSONField()
    suggested_roles = models.JSONField()
    overall_feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Interview {self.interview.id}"
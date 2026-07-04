from django.db import models
from administration.models import Resume, Profile

class QuestionAnswer(models.Model):
    question=models.TextField()
    answer=models.TextField()
    points=models.IntegerField()

    def __str__(self):
        return self.question[:150]

class Analysis(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume=models.ForeignKey(Resume, on_delete=models.CASCADE)    
    scores=models.JSONField()
    strengths=models.JSONField()
    weakness=models.JSONField()
    missing_skills=models.JSONField()
    project_analysis=models.JSONField()
    suggested_roles=models.JSONField()

    def __str__(self):
        return self.resume.__str__
    

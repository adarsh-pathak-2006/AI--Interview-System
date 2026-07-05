from django.db import models
from administration.models import Resume, Profile

class QuestionAnswer(models.Model):
    resume=models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)
    question=models.TextField(blank=True)
    user_answer=models.TextField(blank=True)
    real_answer=models.TextField(blank=True)
    points=models.IntegerField(blank=True)

    def __str__(self):
        return self.question[:150]
    

class Analysis(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    QuestionSet=models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE, null=True)    
    scores=models.JSONField()
    strengths=models.JSONField()
    weakness=models.JSONField()
    missing_skills=models.JSONField()
    project_analysis=models.JSONField()
    suggested_roles=models.JSONField()

    def __str__(self):
        return self.resume.__str__
    
class Interview(models.Model):
    resume=models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    questionanswerset=models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)
    analysis=models.OneToOneField(Analysis, on_delete=models.CASCADE)

    def __str__(self):
        return self.questionanswerset.id
    

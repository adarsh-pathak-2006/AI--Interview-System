from django.contrib import admin
from ai.models import Interview, Question, Answer, Analysis

admin.site.register(Interview)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Analysis)
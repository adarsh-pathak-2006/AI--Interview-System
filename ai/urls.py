from django.urls import path
from ai.views import StartInterviewAPI, AnswerQuestionAPI, FinishInterviewAPI

urlpatterns = [
    path('start/', StartInterviewAPI.as_view(), name='start_interview'),
    path('answer/', AnswerQuestionAPI.as_view(), name='answer_question'),
    path('finish/<int:interview_id>/', FinishInterviewAPI.as_view(), name='finish_interview'),
]

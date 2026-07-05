from django.urls import path
from ai.views import StartInterviewAPI, AnswerQuestionAPI, FinishInterviewAPI, RetrieveInterviewAPI

urlpatterns = [
    path('interview/<int:interview_id>/', RetrieveInterviewAPI.as_view(), name='get_interview'),
    path('start/', StartInterviewAPI.as_view(), name='start_interview'),
    path('answer/', AnswerQuestionAPI.as_view(), name='answer_question'),
    path('finish/<int:interview_id>/', FinishInterviewAPI.as_view(), name='finish_interview'),
]

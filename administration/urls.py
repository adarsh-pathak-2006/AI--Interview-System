from django.urls import path
from administration.views import RegisterAPI, ResumeAPI, ResumeAPIDetail

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('resume/', ResumeAPI.as_view(), name='resume'),
    path('resume/<int:pk>/', ResumeAPIDetail.as_view(), name='resume_individual'),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from administration.views import RegisterAPI, ResumeAPI, ResumeAPIDetail, ProjectAPI, ProjectAPIDetail

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('resume/', ResumeAPI.as_view(), name='resume'),
    path('resume/<int:pk>/', ResumeAPIDetail.as_view(), name='resume_individual'),
    path('project/', ProjectAPI.as_view(), name='project'),
    path('project/<int:pk>/', ProjectAPIDetail.as_view(), name='project_individual'),
]

from django.urls import path
from administration.views import RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
]

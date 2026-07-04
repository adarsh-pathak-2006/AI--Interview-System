from rest_framework.serializers import ModelSerializer
from ai.models import *
from administration.serializers import ProfileSerializer, ResumeSerializer


class QuestionAnswerSerializer(ModelSerializer):
    class Meta:
        model=QuestionAnswer
        fields='__all__'

class AnalysisSerializer(ModelSerializer):
    user=ProfileSerializer(read_only=True)
    resume=ResumeSerializer(read_only=True)
    class Meta:
        model=Analysis
        fields='__all__'
from rest_framework.serializers import ModelSerializer
from ai.models import Interview, Question, Answer, Analysis
from administration.serializers import ResumeSerializer

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['score', 'ai_feedback']

class QuestionSerializer(ModelSerializer):
    answer = AnswerSerializer(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

class AnalysisSerializer(ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'

class InterviewSerializer(ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)
    analysis = AnalysisSerializer(read_only=True)
    
    class Meta:
        model = Interview
        fields = '__all__'
        read_only_fields = ['status']

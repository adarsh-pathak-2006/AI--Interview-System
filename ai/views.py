from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from administration.models import Resume
from ai.models import Interview, Question, Answer, Analysis
from ai.serializers import InterviewSerializer, QuestionSerializer, AnswerSerializer, AnalysisSerializer
from ai.services import generate_interview_questions, evaluate_answer, generate_final_analysis

class StartInterviewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume_id = request.data.get('resume_id')
        if not resume_id:
            return Response({"error": "resume_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        resume = get_object_or_404(Resume, id=resume_id, profile__user=request.user)
        
        # Create Interview
        interview = Interview.objects.create(resume=resume, status='in_progress')
        
        # Generate Questions using AI
        questions_list = generate_interview_questions(resume)
        
        # Save Questions
        created_questions = []
        for i, q_text in enumerate(questions_list):
            q = Question.objects.create(interview=interview, text=q_text, order=i+1)
            created_questions.append(q)
            
        serializer = InterviewSerializer(interview)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnswerQuestionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        question_id = request.data.get('question_id')
        user_answer_text = request.data.get('user_answer')
        
        if not question_id or not user_answer_text:
            return Response({"error": "question_id and user_answer are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        question = get_object_or_404(Question, id=question_id, interview__resume__profile__user=request.user)
        
        # Evaluate using AI
        evaluation = evaluate_answer(question.text, user_answer_text)
        
        answer, created = Answer.objects.update_or_create(
            question=question,
            defaults={
                'user_answer': user_answer_text,
                'score': evaluation.get('score'),
                'ai_feedback': evaluation.get('feedback')
            }
        )
        
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FinishInterviewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, interview_id):
        interview = get_object_or_404(Interview, id=interview_id, resume__profile__user=request.user)
        
        if interview.status == 'completed':
            return Response({"error": "Interview already completed"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Gather all Q&As
        questions = interview.questions.all()
        q_and_a_list = []
        for q in questions:
            if hasattr(q, 'answer'):
                q_and_a_list.append({
                    "question": q.text,
                    "answer": q.answer.user_answer,
                    "score": q.answer.score
                })
        
        # Generate final analysis
        analysis_data = generate_final_analysis(q_and_a_list)
        
        Analysis.objects.create(
            interview=interview,
            scores=analysis_data.get('scores', {}),
            strengths=analysis_data.get('strengths', []),
            weaknesses=analysis_data.get('weaknesses', []),
            missing_skills=analysis_data.get('missing_skills', []),
            project_analysis=analysis_data.get('project_analysis', {}),
            suggested_roles=analysis_data.get('suggested_roles', []),
            overall_feedback=analysis_data.get('overall_feedback', '')
        )
        
        interview.status = 'completed'
        interview.save()
        
        serializer = InterviewSerializer(interview)
        return Response(serializer.data, status=status.HTTP_200_OK)
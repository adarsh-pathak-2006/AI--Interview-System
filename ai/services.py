import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo", # Default fallback model or whatever OpenRouter routes to
        "messages": messages
    }
    
    response = requests.post(OPENROUTER_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['message']['content']

def generate_interview_questions(resume, num_questions=5):
    projects_info = ""
    for proj in resume.projects.all():
        projects_info += f"- {proj.name}: {proj.description}\n"
        
    prompt = f"""
    Act as a senior technical interviewer. 
    You are interviewing a candidate with the following resume summary: {resume.summary}
    Course: {resume.course}
    College: {resume.college}
    CGPA: {resume.cgpa}
    
    Projects:
    {projects_info}
    
    Generate exactly {num_questions} technical interview questions tailored to their resume and projects.
    Return ONLY a JSON list of strings representing the questions, like:
    ["Question 1", "Question 2", "Question 3"]
    """
    
    messages = [{"role": "system", "content": prompt}]
    response_text = call_openrouter(messages)
    
    try:
        # Strip potential markdown formatting like ```json ... ```
        clean_text = response_text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
        return json.loads(clean_text)
    except json.JSONDecodeError:
        # Fallback if AI fails to return strict JSON
        return [q.strip("- ") for q in response_text.split("\n") if q.strip()]

def evaluate_answer(question_text, user_answer):
    prompt = f"""
    Act as a senior technical interviewer.
    The question asked was: "{question_text}"
    The candidate's answer was: "{user_answer}"
    
    Evaluate the answer out of 10.
    Provide constructive feedback.
    
    Return ONLY a JSON object in this exact format:
    {{
        "score": <integer between 0 and 10>,
        "feedback": "<string with feedback>"
    }}
    """
    
    messages = [{"role": "system", "content": prompt}]
    response_text = call_openrouter(messages)
    
    try:
        clean_text = response_text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
        return json.loads(clean_text)
    except json.JSONDecodeError:
        return {"score": 5, "feedback": "Failed to parse AI evaluation: " + response_text}

def generate_final_analysis(q_and_a_list):
    content = ""
    for qa in q_and_a_list:
        content += f"Q: {qa['question']}\nA: {qa['answer']}\nScore: {qa['score']}\n\n"
        
    prompt = f"""
    Act as a senior technical interviewer.
    Here is the transcript of an interview:
    {content}
    
    Analyze the performance. Return ONLY a JSON object in this exact format:
    {{
        "scores": {{"overall": <int>, "technical": <int>, "communication": <int>}},
        "strengths": ["strength 1", "strength 2"],
        "weaknesses": ["weakness 1", "weakness 2"],
        "missing_skills": ["skill 1"],
        "project_analysis": {{"comments": "good"}},
        "suggested_roles": ["role 1"],
        "overall_feedback": "string"
    }}
    """
    
    messages = [{"role": "system", "content": prompt}]
    response_text = call_openrouter(messages)
    
    try:
        clean_text = response_text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
        return json.loads(clean_text)
    except json.JSONDecodeError:
        return {
            "scores": {"overall": 0}, "strengths": [], "weaknesses": [], 
            "missing_skills": [], "project_analysis": {}, "suggested_roles": [],
            "overall_feedback": "Failed to parse AI response."
        }

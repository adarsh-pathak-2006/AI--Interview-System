# AI Interview Platform - Backend API 🚀

This is the backend API for the AI Interview Platform. It is built using **Django** and the **Django REST Framework (DRF)**, providing secure authentication, user profiling, and dynamic AI interview generation via the OpenRouter API.

## 🛠 Tech Stack
- **Framework**: Django & Django REST Framework
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **Authentication**: JWT (JSON Web Tokens) via `djangorestframework-simplejwt`
- **AI Integration**: OpenRouter API
- **Networking**: `django-cors-headers`

## 🌟 Key Features
- **Secure Authentication**: JWT-based login and registration.
- **Resume & Project Management**: Store and retrieve user educational background and technical projects.
- **Dynamic AI Interviews**: Generate personalized technical questions based on the user's specific resume and tech stack.
- **Real-Time Evaluation**: The AI acts as a senior engineer, evaluating answers out of 10 and providing actionable feedback.
- **Comprehensive Analysis**: Generates a final JSON report highlighting strengths, weaknesses, and missing skills.

## 🚀 Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adarsh-pathak-2006/AI--Interview-System.git
   cd AI--Interview-System
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

5. **Run Migrations & Start Server:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
   The backend will be available at `http://localhost:8000`.

## 📡 API Endpoints
- `POST /auth/register/` - Register a new user
- `POST /auth/login/` - Obtain JWT tokens
- `GET /auth/resume/` - Fetch user resumes
- `POST /ai/start/` - Start a new interview session
- `POST /ai/answer/` - Submit an answer to the AI

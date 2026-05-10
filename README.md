SHL Assessment Recommender
AI-Powered Conversational Assessment Recommendation System

An AI-powered conversational recommendation system that helps recruiters and hiring managers discover the most suitable SHL assessments using natural language queries.

Built as part of the SHL AI Intern Take-Home Assignment.

Live API
Swagger Documentation

https://shl-assessment-recommender-6z9a.onrender.com/docs

Health Endpoint

https://shl-assessment-recommender-6z9a.onrender.com/health

Features
Conversational SHL assessment recommendation
FastAPI backend
Gemini AI integration
REST API endpoints
Swagger/OpenAPI documentation
Cloud deployment using Render
Health monitoring endpoint
JSON response handling
API Endpoints
GET /health

Checks whether the API is running successfully.

Example Response
{
  "status": "ok"
}
POST /recommend

Returns SHL assessment recommendations based on user queries.

Request Body
{
  "query": "I need a cognitive ability assessment for software engineers"
}
Example Response
{
  "response": "Recommended SHL assessments for software engineers..."
}
Tech Stack
Python
FastAPI
Gemini API
Uvicorn
Render
Swagger UI
Project Structure
shl-assessment-recommender/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   │   └── llm_service.py
│   └── models/
│
├── requirements.txt
├── Dockerfile
└── README.md
Installation
Clone Repository
git clone https://github.com/Saireddy81797/shl-assessment-recommender.git
cd shl-assessment-recommender
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
Run Locally
uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs
Deployment
Live Deployment

https://shl-assessment-recommender-6z9a.onrender.com/docs

Assignment Overview

This project follows the SHL AI Intern assignment requirements:

Conversational assessment recommendation
FastAPI service implementation
Stateless API design
Structured recommendation responses
Health endpoint support
Cloud deployment support
Sample Query
{
  "query": "Recommend personality and aptitude tests for backend developers"
}
Author
Sai Reddy

GitHub Repository:

https://github.com/Saireddy81797/shl-assessment-recommender

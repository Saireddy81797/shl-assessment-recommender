# SHL Assessment Recommender

## AI-Powered Conversational Assessment Recommendation System

An AI-powered conversational recommendation system that helps recruiters and hiring managers discover the most suitable SHL assessments using natural language queries.

Built as part of the SHL AI Intern Take-Home Assignment.

---

# Live API

## Swagger Documentation

https://shl-assessment-recommender-6z9a.onrender.com/docs

## Health Endpoint

https://shl-assessment-recommender-6z9a.onrender.com/health

---

# Features

- Conversational SHL assessment recommendation
- FastAPI backend
- Gemini AI integration
- REST API endpoints
- Swagger/OpenAPI documentation
- Cloud deployment using Render
- Health monitoring endpoint
- JSON response handling

---

# API Endpoints

## GET /health

Checks whether the API is running successfully.

### Example Response

```json

POST /recommend

Returns SHL assessment recommendations based on user queries.

Request Body

{
  "status": "ok"
}

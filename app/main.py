from fastapi import FastAPI
from pydantic import BaseModel
from app.services.llm_service import generate_response

app = FastAPI(title="SHL Assessment Recommender")


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/recommend")
def recommend(data: QueryRequest):
    response = generate_response(data.query)
    return {"response": response}

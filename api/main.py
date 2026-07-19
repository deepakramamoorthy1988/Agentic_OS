from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import create_plan

app = FastAPI(
    title="Agentic OS",
    description="Enterprise Multi-Agent AI Operating System",
    version="1.0.0"
)


class GoalRequest(BaseModel):
    goal: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Agentic OS 🚀",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/plan")
def planner(request: GoalRequest):

    plan = create_plan(request.goal)

    return {
        "goal": request.goal,
        "plan": plan
    }
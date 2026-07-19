from fastapi import FastAPI
from pydantic import BaseModel

from orchestrator.router import AgentRouter


app = FastAPI(
    title="Agentic OS",
    description="Enterprise Multi-Agent AI Operating System",
    version="1.0.0"
)

# Create router object
router = AgentRouter()


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


@app.post("/execute")
def execute(request: GoalRequest):

    result = router.execute(request.goal)

    return result
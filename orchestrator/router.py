from agents.planner import PlannerAgent
from agents.azure import AzureAgent
from agents.devops import DevOpsAgent
from agents.developer import DeveloperAgent
from agents.reviewer import ReviewerAgent


class AgentRouter:

    def __init__(self):

        self.planner = PlannerAgent()
        self.azure = AzureAgent()
        self.devops = DevOpsAgent()
        self.developer = DeveloperAgent()
        self.reviewer = ReviewerAgent()

    def execute(self, goal: str):

        plan = self.planner.plan(goal)

        return {
            "goal": goal,
            "plan": plan,
            "azure": self.azure.execute(goal),
            "devops": self.devops.execute(goal),
            "developer": self.developer.execute(goal),
            "reviewer": self.reviewer.execute(goal),
        }
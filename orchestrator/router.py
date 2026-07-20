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

        print("Planner...")
        plan = self.planner.plan(goal)
        print("Planner Done")

        print("Azure...")
        azure = self.azure.execute(goal, plan)
        print("Azure Done")

        print("DevOps...")
        devops = self.devops.execute(goal, azure)
        print("DevOps Done")

        print("Developer...")
        developer = self.developer.execute(goal, devops)
        print("Developer Done")

        print("Reviewer...")
        reviewer = self.reviewer.execute(goal, developer)
        print("Reviewer Done")

        return {
            "goal": goal,
            "plan": plan,
            "azure": azure,
            "devops": devops,
            "developer": developer,
            "reviewer": reviewer
        }
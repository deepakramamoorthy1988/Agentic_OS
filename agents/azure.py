from ollama import chat


class AzureAgent:

    def execute(self, goal, context=""):

        prompt = f"""
You are a Microsoft Azure Solution Architect.

You have received an execution plan from the Planner Agent.

Planner Output:

{context}

User Goal:

{goal}

Your task:

- Design the Azure architecture.
- Recommend Azure services.
- Explain deployment order.
- Keep the response concise.
"""

        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content
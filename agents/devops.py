from ollama import chat


class DevOpsAgent:

    def execute(self, goal, context=""):

        prompt = f"""
You are a Senior Azure DevOps Engineer.

You have received the Azure architecture from the Azure Agent.

Azure Architecture:

{context}

User Goal:

{goal}

Your task:

- Design the CI/CD pipeline.
- Explain deployment strategy.
- Recommend Azure DevOps services.
- Mention Terraform, Git, and deployment flow.
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
from ollama import chat


class AzureAgent:

    def execute(self, goal: str):

        prompt = f"""
You are a Microsoft Azure Solution Architect.

For the following goal:

{goal}

Return:

1. Azure Services
2. Resource Architecture
3. Deployment Order

Keep the answer short.

No code.

Plain text.
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
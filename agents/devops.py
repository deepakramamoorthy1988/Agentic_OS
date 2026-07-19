from ollama import chat


class DevOpsAgent:

    def execute(self, goal: str):

        prompt = f"""
You are a Senior Azure DevOps Engineer.

Goal:
{goal}

Provide:

1. CI/CD Pipeline
2. Tools Required
3. Deployment Steps

Keep it short.

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
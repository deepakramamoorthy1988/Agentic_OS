from ollama import chat


class DeveloperAgent:

    def execute(self, goal: str):

        prompt = f"""
You are a Senior Python Software Engineer.

Goal:
{goal}

Provide:

1. Project Structure
2. Required Files
3. Technology Stack

Keep it concise.

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
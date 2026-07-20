from ollama import chat


class DeveloperAgent:

    def execute(self, goal, context=""):

        prompt = f"""
You are a Senior Python and Cloud Application Developer.

You have received the DevOps implementation strategy.

DevOps Strategy:

{context}

User Goal:

{goal}

Your task:

- Design the project structure.
- Recommend technologies.
- Suggest application architecture.
- Recommend folder structure.
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
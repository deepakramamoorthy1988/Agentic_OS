from ollama import chat


class ReviewerAgent:

    def execute(self, goal, context=""):

        prompt = f"""
You are a Senior Cloud Solution Reviewer.

You have received the application design from the Developer Agent.

Developer Design:

{context}

User Goal:

{goal}

Your task:

- Review the overall solution.
- Identify security risks.
- Suggest best practices.
- Recommend improvements.
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
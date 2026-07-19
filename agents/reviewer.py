from ollama import chat


class ReviewerAgent:

    def execute(self, goal: str):

        prompt = f"""
You are a Senior Cloud Security and Code Review Engineer.

Goal:
{goal}

Review the proposed solution.

Return:

1. Security Checks
2. Best Practices
3. Risks
4. Improvements

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
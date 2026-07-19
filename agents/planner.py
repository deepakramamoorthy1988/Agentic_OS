from ollama import chat


def create_plan(goal: str):

    prompt = f"""
You are a Senior Solution Architect.

Create an execution plan.

Rules:

- Return only 8 numbered steps.
- Keep every step under 15 words.
- Do NOT write explanations.
- Do NOT generate code.
- Do NOT use markdown.
- Return plain text only.

Goal:

{goal}
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
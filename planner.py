from openai import OpenAI
from config import MODEL_NAME

client = OpenAI()

class Planner:
    def create_plan(self, goal, memory):
        prompt = f"""
You are an autonomous AI agent.
Goal: {goal}
Previous context: {memory}

Break the goal into a clear, step-by-step plan.
Return numbered steps only.
"""
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

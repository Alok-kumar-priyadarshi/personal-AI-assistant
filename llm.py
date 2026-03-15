import os
from groq import Groq
from dotenv import load_dotenv
from memory_manager import get_memory


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def build_memory_prompt(memory):

    if not memory:
        return "No stored user information."

    context = []

    if memory.get("name"):
        context.append(f"User name: {memory['name']}")

    if memory.get("goals"):
        goals = ", ".join(memory["goals"])
        context.append(f"User goals: {goals}")

    prefs = memory.get("preferences", {})

    if prefs.get("programming_languages"):
        langs = ", ".join(prefs["programming_languages"])
        context.append(f"Preferred programming languages: {langs}")

    if prefs.get("topics"):
        topics = ", ".join(prefs["topics"])
        context.append(f"Interested topics: {topics}")

    return "\n".join(context)


def generate_response(user_input, history):

    memory = get_memory()

    memory_prompt = build_memory_prompt(memory)

    system_prompt = f"""
You are a highly intelligent personal AI assistant.

User Profile:
{memory_prompt}

Guidelines:
- Personalize explanations using the user profile.
- Use preferred programming languages in examples.
- Align suggestions with the user's goals.
- Be concise but helpful.
- Do not say "based on memory".
"""

    messages = [{"role": "system", "content": system_prompt}]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    return response.choices[0].message.content



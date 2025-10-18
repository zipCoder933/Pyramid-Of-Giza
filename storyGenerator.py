# https://ai.google.dev/gemini-api/docs/text-generation

# Getting started
# https://ai.google.dev/gemini-api/docs/quickstart
# pip install -q -U google-genai

from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyAURPgv77N19zLfHWiBPzKhh24DaGyxqHE")

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),  # Disables thinking
        system_instruction="You are a cat. Your name is Neko.",
    ),
)

response = chat.send_message("I have 2 dogs in my house.")

print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

# for message in chat.get_history():
#     print(f"role - {message.role}", end=": ")
#     print(message.parts[0].text)


# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="How does AI work?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=0),  # Disables thinking
#         system_instruction="You are a cat. Your name is Neko.",
#     ),
# )
# print(response.text)

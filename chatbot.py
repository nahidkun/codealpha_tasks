from google import genai
from dotenv import load_dotenv
import os
import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)

load_dotenv()

client = genai.Client()
print("Welcome to the AI chatbot! Type 'exit' to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input
    )

    print(f"AI Response:", response.text)
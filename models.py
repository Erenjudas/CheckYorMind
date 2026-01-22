from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Client initialize karein
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("--- Available Models List ---")
try:
    # 'supported_methods' ki jagah 'supported_actions' use karein
    for m in client.models.list():
        print(f"Model Name: {m.name}")
        print(f"Actions: {m.supported_actions}\n")
except Exception as e:
    print(f"Error: {e}")
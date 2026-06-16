import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Chatbot ready! Type your question and press Enter.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )
    
    print(f"\nGemini: {response.text}\n")
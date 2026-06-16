import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("ERROR: API key not found in .env file")
else:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Scold ALi Bazai for arguing unnecessarily on everything and don't follow western culture blindly. specially drake. in roman urdu in 1 sentence."
    )
    print("Gemini works:", response.text)
    print("\nEnvironment fully ready. Let's build")
import os
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load environment variables from .env file
load_dotenv()
print("✅ Environment variables loaded.")

# ✅ Configure Gemini API with your API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY is not set in the .env file.")

genai.configure(api_key=api_key)

# ✅ Choose model: use "gemini-1.5-flash" for speed or "gemini-1.5-pro" for accuracy
MODEL_NAME = "gemini-1.5-flash-latest"

def generate_response(prompt):
    """
    Generate a response using Gemini API.
    """
    try:
        print("🧠 Using Gemini Model:", MODEL_NAME)

        # Create model object
        model = genai.GenerativeModel(MODEL_NAME)

        # Generate content from the prompt
        print("📤 Sending prompt to Gemini...")
        response = model.generate_content(prompt)

        # Return the generated text
        print("📦 Response received.")
        return response.text.strip()

    except Exception as e:
        print("[❌ Error in generate_response]:", str(e))
        raise

import os
import requests
from dotenv import load_dotenv
load_dotenv()
print("✅ Environment variables loaded:")
print("🧠 HF_MODEL_ID:", os.getenv("HF_MODEL_ID"))

def get_iam_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={os.getenv('IBM_API_KEY')}"
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
        "Content-Type": "application/json"
    }
    model_id = os.getenv("HF_MODEL_ID")
    url = f"https://api-inference.huggingface.co/models/{model_id}"
    
    payload = {"inputs": prompt}
    
    try:
        print("🌍 Sending request to:", url)
        response = requests.post(url, headers=headers, json=payload, timeout=300)
        print("📦 Status Code:", response.status_code)
        print("📦 Raw Response:", response.text)
        
        response.raise_for_status()
        data = response.json()

        if isinstance(data, dict) and "error" in data:
            raise Exception("❌ Hugging Face Error: " + data["error"])

        return data[0]["generated_text"].strip()
        
    except Exception as e:
        print("[❌ Error in generate_response]:", str(e))
        raise
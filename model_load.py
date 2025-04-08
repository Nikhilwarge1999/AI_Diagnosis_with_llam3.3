import os
from dotenv import load_dotenv
from openai import OpenAI
from prompt_template import get_medical_system_prompt

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def generate_diagnosis_response(symptoms):
    messages = [
        {"role": "system", "content": get_medical_system_prompt()},
        {"role": "user", "content": f"My symptoms are: {symptoms}"}
    ]

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.4,
            max_tokens=512,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f" Error: {str(e)}"

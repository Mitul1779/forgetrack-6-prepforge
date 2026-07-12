from google import genai
from dotenv import load_dotenv
import os
from utils.prompts import analysis_prompt

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(
    api_key=api_key
)


def analyze_resume(resume_text):
    prompt = analysis_prompt(resume_text)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
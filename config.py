import os
from dotenv import load_dotenv

load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    UPLOAD_FOLDER = os.path.join(base_dir, "uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024   # 5 MB
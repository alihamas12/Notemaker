import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROVIDER = os.getenv("LLM_PROVIDER", "google")
    
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    UPLOAD_FOLDER = "uploads"
    NOTES_FOLDER = "generated_notes"
    
    def __init__(self):
        if self.PROVIDER == "google" and not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY is required when using Google provider")
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(NOTES_FOLDER, exist_ok=True)

try:
    settings = Settings()
except ValueError as e:
    print(f"Configuration Error: {e}")
    print("Please check your .env file configuration")
    raise

print(f"Using LLM Provider: {settings.PROVIDER}")
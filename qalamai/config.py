import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

# Project Paths 
BASE_DIR        = os.path.dirname(os.path.abspath(__file__))
DOCUMENTS_DIR   = os.path.join(BASE_DIR, "documents")
EXTRACTED_DIR   = os.path.join(BASE_DIR, "extracted_text")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")

# Subjects 
SUBJECTS = {
    "Physics":          "physics",
    "Chemistry":        "chemistry",
    "Biology":          "biology",
    "Mathematics":      "mathematics",
    "Computer Science": "computer_science",
    "English":          "english",
    "Urdu":             "urdu",
    "Pakistan Studies": "pakistan_studies",
    "Islamiat":         "islamiat",
}

# Quiz Settings 
QUIZ_QUESTION_COUNT = 10
QUIZ_TYPES = ["MCQ", "Short Question"]

# Language Settings 
LANGUAGES = ["English", "Urdu"]
DEFAULT_LANGUAGE = "English"

# App Settings 
APP_TITLE    = "QalamAI — FBISE 10th Grade Study Companion"
APP_SUBTITLE = "Ask questions, take quizzes, and get instant feedback in Urdu and English"
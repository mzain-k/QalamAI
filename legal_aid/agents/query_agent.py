"""
Agent 1: Query Understanding Agent
Understands user's legal problem and extracts structured information
"""

import google.generativeai as genai
import json
import re


class QueryUnderstandingAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def analyze(self, user_query: str) -> dict:
        """
        Analyzes the user's legal problem and returns structured data.
        Supports both Urdu and English input.
        """
        prompt = f"""
You are a Pakistani legal intake specialist. Analyze the following legal problem described by a user (may be in Urdu or English) and extract structured information.

User's Problem:
{user_query}

Respond ONLY with a valid JSON object (no markdown, no explanation) with this exact structure:
{{
    "problem_summary": "Brief 1-2 sentence summary in English",
    "legal_category": "One of: Labor Law, Consumer Protection, Property Law, Family Law, Cyber Crime, Criminal Law, Banking & Finance, Other",
    "key_facts": ["fact1", "fact2", "fact3"],
    "urgency_level": "High/Medium/Low",
    "urgency_reason": "Why this urgency level",
    "parties_involved": {{
        "complainant": "Description of the person filing complaint",
        "respondent": "Description of who the complaint is against"
    }},
    "relief_sought": "What outcome the user wants",
    "search_keywords": ["keyword1", "keyword2", "keyword3"],
    "language_detected": "English/Urdu/Mixed"
}}
"""
        try:
            response = self.model.generate_content(prompt)
            raw = response.text.strip()
            # Strip markdown if present
            raw = re.sub(r"```json|```", "", raw).strip()
            return json.loads(raw)
        except Exception as e:
            # Fallback structured response
            return {
                "problem_summary": user_query[:200],
                "legal_category": "Other",
                "key_facts": [user_query],
                "urgency_level": "Medium",
                "urgency_reason": "Unable to auto-analyze, please consult a lawyer",
                "parties_involved": {"complainant": "User", "respondent": "Unknown"},
                "relief_sought": "Legal guidance",
                "search_keywords": user_query.lower().split()[:5],
                "language_detected": "Unknown",
                "error": str(e)
            }

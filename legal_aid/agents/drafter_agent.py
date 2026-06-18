"""
Agent 3: Document Drafter Agent
Drafts legal notices and next-steps action plan
"""

import google.generativeai as genai
from datetime import date


class DocumentDrafterAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def draft_legal_notice(self, query_analysis: dict, law_retrieval: dict) -> str:
        """Drafts a formal legal notice in English."""

        today = date.today().strftime("%d %B, %Y")
        complainant = query_analysis.get("parties_involved", {}).get("complainant", "The Complainant")
        respondent = query_analysis.get("parties_involved", {}).get("respondent", "The Respondent")
        summary = query_analysis.get("problem_summary", "")
        relief = query_analysis.get("relief_sought", "appropriate legal relief")
        legal_analysis = law_retrieval.get("legal_analysis", "")

        prompt = f"""
Draft a formal legal notice for Pakistan in proper legal format.

Details:
- Date: {today}
- Problem: {summary}
- From (Complainant): {complainant}
- To (Respondent): {respondent}
- Relief Sought: {relief}
- Applicable Laws: {legal_analysis[:500]}

Write a professional Pakistani legal notice with:
1. Proper heading (LEGAL NOTICE)
2. Date
3. Parties (From/To with [PLACEHOLDER] for names/addresses)
4. Background facts (numbered)
5. Legal violations committed
6. Relief demanded
7. Consequence of non-compliance (legal action within 14 days)
8. Advocate signature block with [ADVOCATE NAME] placeholder

Use formal legal language. Keep it 300-400 words.
"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error drafting notice: {str(e)}"

    def generate_action_plan(self, query_analysis: dict, law_retrieval: dict) -> str:
        """Generates a step-by-step action plan."""

        prompt = f"""
You are a Pakistani legal advisor. Create a practical step-by-step action plan for this legal problem.

Problem: {query_analysis.get('problem_summary')}
Legal Category: {query_analysis.get('legal_category')}
Urgency: {query_analysis.get('urgency_level')} - {query_analysis.get('urgency_reason')}
Available Remedies: {law_retrieval.get('legal_analysis', '')[:400]}

Create a numbered action plan with:
1. **Immediate Steps (Today/This Week)** - What to do RIGHT NOW
2. **Evidence Collection** - What documents/proof to gather
3. **Legal Steps (Next 2-4 Weeks)** - Filing complaints, sending notices
4. **Court Process (If Needed)** - Which court, estimated timeline, costs
5. **Important Contacts** - Relevant government offices, helplines in Pakistan
6. **Tips for Success** - Practical advice for this type of case

Be specific to Pakistan (mention actual helplines, courts, government bodies).
Format clearly with emojis for each step to make it readable.
"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating action plan: {str(e)}"

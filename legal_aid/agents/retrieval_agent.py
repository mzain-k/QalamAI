"""
Agent 2: Law Retrieval Agent (RAG)
Retrieves relevant Pakistani laws based on the analyzed query
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.legal_kb import LEGAL_KNOWLEDGE
import google.generativeai as genai


class LawRetrievalAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.knowledge_base = LEGAL_KNOWLEDGE

    def _keyword_match_score(self, query_analysis: dict, law_entry: dict) -> float:
        """Simple keyword-based retrieval scoring."""
        score = 0.0
        search_keywords = [k.lower() for k in query_analysis.get("search_keywords", [])]
        problem_text = query_analysis.get("problem_summary", "").lower()
        category = query_analysis.get("legal_category", "").lower()

        # Category match (highest weight)
        if category in law_entry["category"].lower():
            score += 10.0

        # Keyword matches
        for kw in search_keywords:
            for law_kw in law_entry.get("keywords", []):
                if kw in law_kw.lower() or law_kw.lower() in kw:
                    score += 2.0

        # Problem text matches keywords
        for law_kw in law_entry.get("keywords", []):
            if law_kw.lower() in problem_text:
                score += 1.5

        return score

    def retrieve(self, query_analysis: dict) -> dict:
        """Retrieve top relevant laws and generate legal analysis."""

        # Score all knowledge base entries
        scored = []
        for entry in self.knowledge_base:
            score = self._keyword_match_score(query_analysis, entry)
            if score > 0:
                scored.append((score, entry))

        # Sort by score, get top 3
        scored.sort(key=lambda x: x[0], reverse=True)
        top_laws = [entry for _, entry in scored[:3]]

        # If no matches, use all entries and let Gemini decide
        if not top_laws:
            top_laws = self.knowledge_base[:2]

        # Build context for Gemini
        laws_context = "\n\n".join([
            f"=== {law['title']} ({law['category']}) ===\n{law['content']}"
            for law in top_laws
        ])

        prompt = f"""
You are a Pakistani legal expert. Based on the following legal problem analysis and relevant Pakistani laws, provide a comprehensive legal analysis.

PROBLEM ANALYSIS:
- Summary: {query_analysis.get('problem_summary')}
- Category: {query_analysis.get('legal_category')}
- Key Facts: {', '.join(query_analysis.get('key_facts', []))}
- Relief Sought: {query_analysis.get('relief_sought')}

RELEVANT PAKISTANI LAWS:
{laws_context}

Provide a detailed legal analysis in this format:

**APPLICABLE LAWS:**
List the specific laws, sections, and ordinances that apply to this case.

**LEGAL POSITION:**
Explain the user's legal standing and rights under Pakistani law.

**AVAILABLE REMEDIES:**
List all legal remedies available to the user, from most to least recommended.

**RELEVANT AUTHORITIES:**
Which courts, tribunals, or government bodies have jurisdiction.

**TIME LIMITATIONS:**
Any important deadlines or limitation periods the user must be aware of.

Be specific to Pakistani law and be practical in your advice.
"""
        try:
            response = self.model.generate_content(prompt)
            return {
                "retrieved_laws": top_laws,
                "legal_analysis": response.text,
                "categories_found": list(set([law["category"] for law in top_laws]))
            }
        except Exception as e:
            return {
                "retrieved_laws": top_laws,
                "legal_analysis": "Error generating analysis. Please consult a lawyer directly.",
                "categories_found": [],
                "error": str(e)
            }

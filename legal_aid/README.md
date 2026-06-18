# ⚖️ AI Legal Aid Assistant — Pakistan
### National AI Hackathon '26 | atomcamp | Team Project

A multi-agent AI system that helps Pakistani citizens understand their legal rights,
retrieve relevant laws, and draft legal notices — in Urdu or English.

---

## 🏗️ Architecture

```
User Input (Urdu/English)
        │
        ▼
┌─────────────────────────┐
│  Agent 1: Query         │  → Extracts: category, facts, urgency, parties
│  Understanding          │    using Gemini 1.5 Flash
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Agent 2: Law Retrieval │  → Keyword RAG on Pakistani legal KB
│  (RAG Pipeline)         │    + Gemini for legal analysis
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Agent 3: Document      │  → Drafts legal notice + action plan
│  Drafter                │    using Gemini
└────────────┬────────────┘
             │
             ▼
    Streamlit Web UI
```

---

## 📁 Project Structure

```
legal_aid/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md
├── agents/
│   ├── __init__.py
│   ├── query_agent.py      # Agent 1: Query Understanding
│   ├── retrieval_agent.py  # Agent 2: Law Retrieval (RAG)
│   └── drafter_agent.py    # Agent 3: Document Drafter
└── data/
    ├── __init__.py
    └── legal_kb.py         # Pakistani Legal Knowledge Base
```

---

## ⚙️ Setup & Execution Steps

### Step 1: Get Your Gemini API Key
1. Go to → https://aistudio.google.com/
2. Click "Get API Key" → Create API Key
3. Copy the key (starts with `AIza...`)

### Step 2: Install Dependencies
```bash
cd legal_aid
pip install -r requirements.txt
```

> If you face issues, install key packages individually:
```bash
pip install google-generativeai streamlit
```

### Step 3: Run the App
```bash
streamlit run app.py
```

The app opens at: **http://localhost:8501**

### Step 4: Use the App
1. Paste your Gemini API key in the **sidebar**
2. Type your legal problem in **Urdu or English**
3. Or pick a **sample case** from the dropdown
4. Click **"Analyze My Legal Problem"**
5. View results in 3 tabs:
   - 📊 Legal Analysis
   - 📄 Legal Notice (downloadable)
   - 🗺️ Action Plan (downloadable)

---

## 🔑 Environment Variable (Optional)
Instead of entering API key in UI every time, set it as env variable:

**Windows:**
```cmd
set GEMINI_API_KEY=your_key_here
```

**Mac/Linux:**
```bash
export GEMINI_API_KEY=your_key_here
```

---

## 📚 Legal Categories Covered
| # | Category | Laws Referenced |
|---|----------|-----------------|
| 1 | Labor & Employment | Industrial Relations Act 2012, Standing Orders Ordinance 1968 |
| 2 | Consumer Protection | Punjab/Sindh/KPK/Balochistan Consumer Protection Acts |
| 3 | Property & Rent | Transfer of Property Act 1882, Rent Restriction Acts |
| 4 | Family Law | Muslim Family Laws Ordinance 1961, Family Courts Act 1964 |
| 5 | Cyber Crime | PECA 2016 |
| 6 | Criminal Law | Pakistan Penal Code 1860, CrPC 1898 |
| 7 | Banking & Finance | Banking Companies Ordinance 1962 |

---

## 💡 Hackathon Enhancements (Day 2 Ideas)
- [ ] Add ChromaDB for true vector RAG (replace keyword matching)
- [ ] Add PDF upload for legal documents
- [ ] Add Urdu language output (translate notice to Urdu)
- [ ] Add voice input support
- [ ] Connect to actual law databases (Pakistan Law Site API)
- [ ] Add case history tracking

---

## ⚠️ Disclaimer
This tool provides general legal information for educational purposes only.
It does NOT constitute professional legal advice.
Always consult a licensed advocate before taking legal action.

---
*Built for National AI Hackathon '26 by atomcamp — Quetta Regional Round*

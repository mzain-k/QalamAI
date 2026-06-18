"""
AI Legal Aid Assistant for Pakistan
Multi-Agent System: Query Understanding → Law Retrieval (RAG) → Document Drafter
"""

import streamlit as st
import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.query_agent import QueryUnderstandingAgent
from agents.retrieval_agent import LawRetrievalAgent
from agents.drafter_agent import DocumentDrafterAgent

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Legal Aid Pakistan",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .main { background-color: #0f172a; }
    .stApp { background-color: #0f172a; }

    .hero-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #0f2744 100%);
        border: 1px solid #2d5986;
        border-radius: 16px;
        padding: 36px 40px;
        margin-bottom: 28px;
        text-align: center;
    }
    .hero-box h1 {
        color: #e2f0ff;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 8px 0;
    }
    .hero-box p {
        color: #94b8d9;
        font-size: 1.05rem;
        margin: 0;
    }

    .agent-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 16px;
    }
    .agent-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
    }
    .agent-badge {
        background: #1d4ed8;
        color: white;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 20px;
        letter-spacing: 0.5px;
    }
    .agent-title {
        color: #cbd5e1;
        font-weight: 600;
        font-size: 0.95rem;
    }

    .urgency-high { border-left: 4px solid #ef4444 !important; }
    .urgency-medium { border-left: 4px solid #f59e0b !important; }
    .urgency-low { border-left: 4px solid #22c55e !important; }

    .fact-chip {
        display: inline-block;
        background: #1e3a5f;
        color: #93c5fd;
        border: 1px solid #2d5986;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.82rem;
        margin: 3px 3px 3px 0;
    }

    .notice-box {
        background: #111827;
        border: 1px solid #1e40af;
        border-radius: 10px;
        padding: 24px;
        font-family: 'Courier New', monospace;
        font-size: 0.85rem;
        color: #d1d5db;
        white-space: pre-wrap;
        line-height: 1.7;
    }

    .step-section {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px;
    }

    .disclaimer {
        background: #1c1917;
        border: 1px solid #78350f;
        border-radius: 8px;
        padding: 14px 18px;
        color: #d97706;
        font-size: 0.82rem;
        margin-top: 24px;
    }

    .stTextArea textarea {
        background: #1e293b !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        font-size: 0.95rem !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 32px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.2s !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        transform: translateY(-1px) !important;
    }

    div[data-testid="stSidebar"] {
        background: #1e293b !important;
    }
    .sidebar-title { color: #93c5fd; font-weight: 700; font-size: 1rem; }
    .sidebar-item { color: #94a3b8; font-size: 0.85rem; padding: 4px 0; }

    h2, h3 { color: #e2e8f0 !important; }
    p, li { color: #94a3b8; }
    .stMarkdown { color: #94a3b8; }
    label { color: #cbd5e1 !important; }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background: #1e293b;
        border-radius: 10px;
        padding: 4px;
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #64748b !important;
        background: transparent !important;
        border-radius: 8px !important;
    }
    .stTabs [aria-selected="true"] {
        background: #1d4ed8 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="sidebar-title">⚖️ AI Legal Aid Pakistan</p>', unsafe_allow_html=True)
    st.markdown("---")


    api_key = os.getenv("GEMINI_API_KEY")

    # api_key = st.text_input(
    #     "🔑 Gemini API Key",
    #     type="password",
    #     placeholder="AIza...",
    #     help="Get your free key from aistudio.google.com"
    # )

    st.markdown("---")
    st.markdown('<p class="sidebar-title">📚 Legal Categories</p>', unsafe_allow_html=True)
    categories = [
        "⚒️ Labor & Employment",
        "🛒 Consumer Protection",
        "🏠 Property & Rent",
        "👨‍👩‍👧 Family Law",
        "💻 Cyber Crime",
        "🚔 Criminal Law",
        "🏦 Banking & Finance"
    ]
    for cat in categories:
        st.markdown(f'<p class="sidebar-item">{cat}</p>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p class="sidebar-title">🤖 Agent Pipeline</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-item">① Query Understanding</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-item">② Law Retrieval (RAG)</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-item">③ Document Drafter</p>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        '<p class="sidebar-item">Built with 🇵🇰 for National AI Hackathon \'26 by atomcamp</p>',
        unsafe_allow_html=True
    )


# ─── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-box">
    <h1>⚖️ AI Legal Aid Assistant</h1>
    <p>Describe your legal problem in <strong>Urdu or English</strong> — our AI agents analyze Pakistani law and draft your legal notice instantly</p>
</div>
""", unsafe_allow_html=True)


# ─── Input Section ────────────────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    user_problem = st.text_area(
        "📝 Describe Your Legal Problem",
        height=150,
        placeholder="Example: My employer fired me without any notice or reason after 3 years of work. They also haven't paid my last 2 months salary. What can I do?\n\nمثال: میرے مالک مکان نے مجھے بغیر کسی نوٹس کے گھر سے نکال دیا...",
        label_visibility="visible"
    )

with col2:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    sample_cases = {
        "Select a sample...": "",
        "🏢 Wrongful Termination": "My employer fired me without notice after 5 years of service. They haven't paid my last 3 months salary and refused to give me experience certificate. What are my rights?",
        "🏠 Property Dispute": "My neighbor has illegally taken over part of my land (qabza). He claims it's his but I have all the ownership documents. Police are not helping.",
        "💻 Online Fraud": "Someone created a fake profile using my photos and is blackmailing me. I have screenshots as evidence. What action can I take?",
        "👨‍👩‍👧 Divorce & Maintenance": "میں نے طلاق دے دی ہے لیکن بچوں کی ماں نفقہ کا مطالبہ کر رہی ہے۔ بچوں کی تحویل کس کو ملے گی؟",
        "🛒 Consumer Fraud": "I bought a mobile phone worth Rs. 45,000 from a shop. It stopped working after 2 days. The shopkeeper is refusing to replace or refund.",
    }
    selected = st.selectbox("📋 Try a Sample", list(sample_cases.keys()))
    if selected != "Select a sample..." and sample_cases[selected]:
        user_problem = sample_cases[selected]

analyze_btn = st.button("🔍 Analyze My Legal Problem", use_container_width=True)


# ─── Analysis Pipeline ───────────────────────────────────────────────────────
if analyze_btn:
    if not api_key:
        st.error("⚠️ Please enter your Gemini API key in the sidebar.")
    elif not user_problem.strip():
        st.error("⚠️ Please describe your legal problem above.")
    else:
        # Initialize agents
        query_agent = QueryUnderstandingAgent(api_key)
        retrieval_agent = LawRetrievalAgent(api_key)
        drafter_agent = DocumentDrafterAgent(api_key)

        # AGENT 1: Query Understanding
        with st.spinner("🤖 Agent 1: Understanding your problem..."):
            query_result = query_agent.analyze(user_problem)
            time.sleep(0.5)

        # AGENT 2: Law Retrieval
        with st.spinner("📚 Agent 2: Searching Pakistani law database..."):
            law_result = retrieval_agent.retrieve(query_result)
            time.sleep(0.5)

        # AGENT 3: Document Drafting
        with st.spinner("✍️ Agent 3: Drafting legal notice and action plan..."):
            legal_notice = drafter_agent.draft_legal_notice(query_result, law_result)
            action_plan = drafter_agent.generate_action_plan(query_result, law_result)

        st.success("✅ Analysis Complete! Scroll down to see your legal report.")
        st.markdown("---")

        # ── Tabs for Results ─────────────────────────────────────────────────
        tab1, tab2, tab3 = st.tabs(["📊 Legal Analysis", "📄 Legal Notice", "🗺️ Action Plan"])

        # ── Tab 1: Legal Analysis ────────────────────────────────────────────
        with tab1:
            # Agent 1 Output
            urgency = query_result.get("urgency_level", "Medium")
            urgency_class = f"urgency-{urgency.lower()}"

            st.markdown(f"""
            <div class="agent-card {urgency_class}">
                <div class="agent-header">
                    <span class="agent-badge">AGENT 1</span>
                    <span class="agent-title">Query Understanding</span>
                    <span style="margin-left:auto; color:#f59e0b; font-size:0.8rem">⚡ {urgency} Priority</span>
                </div>
            """, unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"**📌 Summary:** {query_result.get('problem_summary', 'N/A')}")
                st.markdown(f"**⚖️ Category:** {query_result.get('legal_category', 'N/A')}")
                st.markdown(f"**🎯 Relief Sought:** {query_result.get('relief_sought', 'N/A')}")
                st.markdown(f"**🌐 Language:** {query_result.get('language_detected', 'N/A')}")
            with col_b:
                st.markdown("**📋 Key Facts:**")
                facts_html = "".join([f'<span class="fact-chip">{f}</span>' for f in query_result.get("key_facts", [])])
                st.markdown(facts_html, unsafe_allow_html=True)
                st.markdown(f"**⚠️ Urgency Reason:** _{query_result.get('urgency_reason', 'N/A')}_")

            st.markdown("</div>", unsafe_allow_html=True)

            # Agent 2 Output
            st.markdown(f"""
            <div class="agent-card">
                <div class="agent-header">
                    <span class="agent-badge">AGENT 2</span>
                    <span class="agent-title">Law Retrieval (RAG)</span>
                    <span style="margin-left:auto; color:#64748b; font-size:0.8rem">
                        📚 {len(law_result.get('retrieved_laws', []))} laws retrieved
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(law_result.get("legal_analysis", "No analysis available."))

            # Show retrieved law titles
            if law_result.get("retrieved_laws"):
                st.markdown("**📖 Laws Referenced:**")
                for law in law_result["retrieved_laws"]:
                    st.markdown(f"- **{law['title']}** _{law['category']}_")

        # ── Tab 2: Legal Notice ──────────────────────────────────────────────
        with tab2:
            st.markdown(f"""
            <div class="agent-card">
                <div class="agent-header">
                    <span class="agent-badge">AGENT 3</span>
                    <span class="agent-title">Legal Notice Draft</span>
                    <span style="margin-left:auto; color:#64748b; font-size:0.8rem">Fill in [PLACEHOLDERS] before use</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f'<div class="notice-box">{legal_notice}</div>', unsafe_allow_html=True)

            st.download_button(
                label="⬇️ Download Legal Notice (.txt)",
                data=legal_notice,
                file_name=f"legal_notice_{query_result.get('legal_category', 'general').replace(' ', '_').lower()}.txt",
                mime="text/plain",
                use_container_width=True
            )

        # ── Tab 3: Action Plan ───────────────────────────────────────────────
        with tab3:
            st.markdown(f"""
            <div class="agent-card">
                <div class="agent-header">
                    <span class="agent-badge">AGENT 3</span>
                    <span class="agent-title">Step-by-Step Action Plan</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(action_plan)

            st.download_button(
                label="⬇️ Download Full Report (.txt)",
                data=f"LEGAL ANALYSIS REPORT\n{'='*50}\n\nPROBLEM:\n{user_problem}\n\n{'='*50}\nLEGAL ANALYSIS:\n{law_result.get('legal_analysis')}\n\n{'='*50}\nLEGAL NOTICE:\n{legal_notice}\n\n{'='*50}\nACTION PLAN:\n{action_plan}",
                file_name="legal_aid_full_report.txt",
                mime="text/plain",
                use_container_width=True
            )

        # ── Disclaimer ───────────────────────────────────────────────────────
        st.markdown("""
        <div class="disclaimer">
            ⚠️ <strong>Legal Disclaimer:</strong> This AI tool provides general legal information based on Pakistani law for educational purposes only.
            It does NOT constitute professional legal advice. Please consult a licensed advocate before taking legal action.
            For emergencies, contact <strong>Pakistan Bar Council: 051-9211573</strong> or your nearest district bar association.
        </div>
        """, unsafe_allow_html=True)


# ─── Empty State ─────────────────────────────────────────────────────────────
else:
    st.markdown("""
    <div style="text-align:center; padding: 40px 20px; color: #475569;">
        <div style="font-size: 3rem; margin-bottom: 16px;">⚖️</div>
        <p style="font-size: 1.1rem; color: #64748b;">
            Enter your legal problem above and click <strong style="color:#3b82f6">Analyze</strong> to get started
        </p>
        <p style="font-size: 0.85rem; color: #334155; margin-top: 8px;">
            Supports English and Urdu • Covers 7 areas of Pakistani law • Generates legal notice + action plan
        </p>
    </div>
    """, unsafe_allow_html=True)

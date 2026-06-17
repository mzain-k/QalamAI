import gradio as gr
from agents import get_tutor_agent, get_quiz_agent, get_feedback_agent
from quiz import new_session, generate_quiz, parse_quiz, record_answer, generate_feedback
from crewai import Task, Crew
from config import SUBJECTS, LANGUAGES, APP_TITLE

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --ink: #1B2A4A;
    --ink-light: #2E4373;
    --parchment: #FFF8ED;
    --gold: #E8A33D;
    --gold-deep: #C9821F;
    --green: #1F6F50;
    --coral: #E76F51;
}

.gradio-container {
    background: var(--parchment) !important;
    font-family: 'Inter', sans-serif !important;
}

#header-block {
    background: linear-gradient(135deg, var(--ink) 0%, var(--ink-light) 100%);
    border-radius: 16px;
    padding: 26px 32px;
    margin-bottom: 16px;
}

#header-title {
    font-family: 'Lora', serif !important;
    font-size: 30px !important;
    font-weight: 700 !important;
    color: #FFF8ED !important;
    margin: 0 !important;
}

#header-title .qalam-mark { color: var(--gold) !important; }

#header-subtitle {
    font-size: 14px !important;
    color: #C7D2E8 !important;
    margin-top: 4px !important;
}

.section-card {
    background: white;
    border: 1px solid #EFE3CC;
    border-radius: 14px;
    padding: 18px;
}

.section-label {
    font-family: 'Lora', serif !important;
    font-weight: 600 !important;
    font-size: 14.5px !important;
    color: #1B2A4A !important;
    border-left: 3px solid #E8A33D;
    padding-left: 10px;
    margin-bottom: 8px !important;
    opacity: 1 !important;
}

.section-label p {
    color: #1B2A4A !important;
    opacity: 1 !important;
}

.tabs button {
    color: #1B2A4A !important;
    opacity: 0.6;
    font-weight: 500 !important;
}

.tabs button.selected {
    color: var(--gold-deep) !important;
    opacity: 1 !important;
    font-weight: 600 !important;
}

#ask-btn, #start-quiz-btn, #submit-answer-btn {
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-deep) 100%) !important;
    color: var(--ink) !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 10px !important;
}

#finish-quiz-btn {
    background: var(--ink) !important;
    color: var(--parchment) !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 10px !important;
}

footer {visibility: hidden}
"""

SUBJECT_LIST = list(SUBJECTS.keys())

def ask_question(subject, language, question):
    if not question.strip():
        return "Please type a question first."

    agent = get_tutor_agent(subject, language)
    task = Task(
        description=f"""A student is asking about {subject}:
        
        Question: {question}
        
        Answer clearly and simply, suitable for a 10th grade student. 
        Respond in {language}.""",
        expected_output=f"A clear, helpful explanation in {language}.",
        agent=agent
    )
    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    result = crew.kickoff()
    return result.raw


def start_quiz(subject, language):
    raw_output = generate_quiz(subject, language, context="")
    questions, correct_answers = parse_quiz(raw_output)

    session = new_session(subject, language)
    session["questions"] = questions
    session["correct_answers_key"] = correct_answers
    session["active"] = True
    session["current_index"] = 0

    if not questions:
        return session, "Could not generate quiz. Please try again.", gr.update(visible=False), gr.update(visible=True)

    first_q = questions[0]
    progress = f"Question 1 of {len(questions)}"
    return session, f"{progress}\n\n{first_q}", gr.update(visible=True), gr.update(visible=False)


def submit_answer(session, student_answer):
    idx = session["current_index"]
    correct = session["correct_answers_key"][idx]

    session = record_answer(session, student_answer, correct)
    session["current_index"] += 1

    total_q = len(session["questions"])

    if session["current_index"] >= total_q:
        session["active"] = False
        score_text = f"Quiz complete! Score: {session['score']} / {session['total']}"
        return session, score_text, "", gr.update(visible=False), gr.update(visible=True)

    next_q = session["questions"][session["current_index"]]
    progress = f"Question {session['current_index'] + 1} of {total_q}"
    return session, f"{progress}\n\n{next_q}", "", gr.update(visible=True), gr.update(visible=False)


def get_feedback_report(session):
    feedback = generate_feedback(session, session["questions"])
    return feedback


with gr.Blocks(css=CUSTOM_CSS, theme=gr.themes.Soft(primary_hue="orange"), title="QalamAI") as demo:

    quiz_session = gr.State(value={})

    with gr.Column(elem_id="header-block"):
        gr.HTML("""
            <div id="header-title">Qalam<span class="qalam-mark">AI</span> 🖊️</div>
            <div id="header-subtitle">Your FBISE 10th Grade Study Companion — Ask, Practice, Improve</div>
        """)

    with gr.Row():
        with gr.Column(scale=1, elem_classes="section-card"):
            gr.Markdown("Subject", elem_classes="section-label")
            subject = gr.Dropdown(choices=SUBJECT_LIST, value="Physics", container=False)

            gr.Markdown("Language", elem_classes="section-label")
            language = gr.Radio(choices=LANGUAGES, value="English", container=False)

        with gr.Column(scale=2, elem_classes="section-card"):
            with gr.Tab("Ask a Question"):
                question_input = gr.Textbox(
                    placeholder="e.g. Explain Newton's Second Law of Motion",
                    lines=3, container=False
                )
                ask_btn = gr.Button("Ask QalamAI", elem_id="ask-btn", size="lg")
                answer_output = gr.Textbox(lines=8, interactive=False, container=False, label=None)

                ask_btn.click(
                    fn=ask_question,
                    inputs=[subject, language, question_input],
                    outputs=[answer_output]
                )

            with gr.Tab("Take a Quiz"):
                start_quiz_btn = gr.Button("Start Quiz", elem_id="start-quiz-btn", size="lg")

                quiz_display = gr.Textbox(lines=8, interactive=False, container=False, label=None)

                with gr.Column(visible=False) as answer_row:
                    answer_input = gr.Textbox(
                        placeholder="Type A, B, C, or D",
                        container=False
                    )
                    submit_answer_btn = gr.Button("Submit Answer", elem_id="submit-answer-btn")

                with gr.Column(visible=False) as feedback_row:
                    finish_btn = gr.Button("Get My Feedback Report", elem_id="finish-quiz-btn", size="lg")
                    feedback_output = gr.Textbox(lines=12, interactive=False, container=False, label=None)

                start_quiz_btn.click(
                    fn=start_quiz,
                    inputs=[subject, language],
                    outputs=[quiz_session, quiz_display, answer_row, feedback_row]
                )

                submit_answer_btn.click(
                    fn=submit_answer,
                    inputs=[quiz_session, answer_input],
                    outputs=[quiz_session, quiz_display, answer_input, answer_row, feedback_row]
                )

                finish_btn.click(
                    fn=get_feedback_report,
                    inputs=[quiz_session],
                    outputs=[feedback_output]
                )

demo.launch()
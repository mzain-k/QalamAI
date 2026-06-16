from crewai import Task, Crew
from agents import get_quiz_agent, get_feedback_agent
from config import QUIZ_QUESTION_COUNT

# Session State 
def new_session(subject, language):
    return {
        "subject":          subject,
        "language":         language,
        "questions":        [],
        "correct_answers":  [],
        "student_answers":  [],
        "score":            0,
        "total":            0,
        "active":           False,
        "feedback_done":    False,
    }

# Generate Quiz 
def generate_quiz(subject, language, context):
    agent = get_quiz_agent(subject, language)

    task = Task(
        description=f"""Generate exactly {QUIZ_QUESTION_COUNT} quiz questions 
        for FBISE 10th grade {subject}.
        
        Use this context from the textbook and past papers:
        {context}
        
        Format your response EXACTLY like this for every question:
        
        Q1: [question text]
        A) [option]
        B) [option]
        C) [option]
        D) [option]
        Correct Answer: [A/B/C/D]
        
        Q2: ...and so on.
        
        Generate all {QUIZ_QUESTION_COUNT} questions in {language}.""",
        expected_output=f"""{QUIZ_QUESTION_COUNT} clearly formatted MCQ questions 
        with 4 options each and correct answers marked.""",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    result = crew.kickoff()
    return result.raw

# Parse Quiz Output 
def parse_quiz(raw_output):
    questions = []
    correct_answers = []

    blocks = raw_output.strip().split("\n\n")

    for block in blocks:
        lines = block.strip().split("\n")
        if not lines:
            continue

        question_lines = []
        correct = None

        for line in lines:
            if line.startswith("Correct Answer:"):
                correct = line.replace("Correct Answer:", "").strip()
            else:
                question_lines.append(line)

        if question_lines and correct:
            questions.append("\n".join(question_lines))
            correct_answers.append(correct)

    return questions, correct_answers

# Record Answer 
def record_answer(session, student_answer, correct_answer):
    session["student_answers"].append(student_answer.strip().upper())
    session["correct_answers"].append(correct_answer.strip().upper())
    session["total"] += 1

    if student_answer.strip().upper() == correct_answer.strip().upper():
        session["score"] += 1

    return session

# Generate Feedback 
def generate_feedback(session, questions_text):
    subject  = session["subject"]
    language = session["language"]
    agent    = get_feedback_agent(subject, language)

    # Build results summary
    results = []
    for i, (q, ca, sa) in enumerate(zip(
        questions_text,
        session["correct_answers"],
        session["student_answers"]
    )):
        status = "Correct" if ca == sa else "Wrong"
        results.append(
            f"Q{i+1}: {q}\n"
            f"Correct Answer: {ca}\n"
            f"Student Answer: {sa}\n"
            f"Result: {status}"
        )

    results_text = "\n\n".join(results)
    score = session["score"]
    total = session["total"]

    task = Task(
        description=f"""A student just completed a {subject} quiz.
        
        Score: {score} out of {total}
        
        Detailed Results:
        {results_text}
        
        Please provide in {language}:
        1. A brief encouraging opening based on the score
        2. For every WRONG answer — clear simple explanation of the correct answer
        3. List of weak topics identified from the mistakes
        4. 2-3 specific study tips for improvement
        5. A motivating closing message""",
        expected_output=f"""Complete feedback report in {language} with 
        explanations for wrong answers, weak topics, and study tips.""",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    result = crew.kickoff()
    return result.raw
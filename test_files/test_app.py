import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, LLM
import gradio as gr


load_dotenv()

llm = LLM(
    model = "gemini/gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)


# Agents
researcher = Agent(
    role="Research Analyst",
    goal="Research the given topic and extract the most important information",
    backstory="""You are a senior research analyst with expertise in finding 
    and summarizing complex information clearly.""",
    llm=llm,
    verbose=False
)

writer = Agent(
    role="Content Writer",
    goal="Transform research findings into a clear, engaging, well structured report",
    backstory="""You are a professional writer who specializes in turning raw 
    research into polished, readable content.""",
    llm=llm,
    verbose=False
)

reviewer = Agent(
    role="Quality Reviewer",
    goal="Review the written report and provide a quality verdict with suggestions",
    backstory="""You are a strict but fair quality reviewer who checks reports 
    for clarity, completeness, and accuracy.""",
    llm=llm,
    verbose=False
)


# Core Function - Crew will run
def run_crew(topic):
    if not topic.strip():
        return "Please enter a topic.", "", ""

    research_task = Task(
        description=f"Research this topic thoroughly: {topic}",
        expected_output="A detailed research summary with key facts and insights",
        agent=researcher
    )

    writing_task = Task(
        description="Using the research provided, write a polished structured report",
        expected_output="A complete report with Title, Introduction, Key Findings, and Conclusion",
        agent=writer,
        context=[research_task]
    )

    review_task = Task(
        description="Review the written report for quality, clarity and completeness",
        expected_output="A review with Quality Score, Strengths, Weaknesses, Final Verdict",
        agent=reviewer,
        context=[writing_task]
    )

    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks=[research_task, writing_task, review_task],
        verbose=False
    )

    crew.kickoff()

    research_output = research_task.output.raw
    writing_output  = writing_task.output.raw
    review_output   = review_task.output.raw

    return research_output, writing_output, review_output


# Gradio UI
with gr.Blocks(title = "Multi Agent Research System") as app:
    gr.Markdown("# Multi-Agent Research System")
    gr.Markdown("Enter a topic and three AI agents will research, write, and review a report.")

    with gr.Row():
        topic_input = gr.Textbox(
            label = "Topic",
            placeholder = "e.g. Multi Agent RAG Systems",
            scale = 4
        )
        run_button = gr.Button("Run Agents", variant = "primary", scale = 1)

    with gr.Row():
        research_out = gr.Textbox(label="Agent 1 — Researcher", lines=10)
        writing_out  = gr.Textbox(label="Agent 2 — Writer",     lines=10)
        review_out   = gr.Textbox(label="Agent 3 — Reviewer",   lines=10)

    run_button.click(
        fn = run_crew,
        inputs = [topic_input],
        outputs = [research_out, writing_out, review_out]
    )

app.launch()
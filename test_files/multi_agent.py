import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

# Connect Gemini to CrewAI
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Three Agents
researcher = Agent(
    role="Research Analyst",
    goal="Research the given topic and provide a detailed, structured summary",
    backstory="""You are a senior research analyst with expertise in finding 
    and summarizing complex information clearly. You always provide factual, 
    well structured findings.""",
    llm=llm,
    verbose=True
)
writer = Agent(
    role="Content Writer",
    goal="Transform research findings into a clear, engaging, well structured report",
    backstory="""You are a professional writer who specializes in turning raw 
    research into polished, readable content. You always write in a clear 
    structure with headings and bullet points.""",
    llm=llm,
    verbose=True
)
reviewer = Agent(
    role="Quality Reviewer",
    goal="Review the written report and provide a quality verdict with suggestions",
    backstory="""You are a strict but fair quality reviewer. You check reports 
    for clarity, completeness, and accuracy. You always give a score out of 10 
    and specific suggestions for improvement.""",
    llm=llm,
    verbose=True
)


# Assigning tasks
topic = input("Enter a topic to research: ")

research_task = Task(
    description=f"Research this topic thoroughly: {topic}",
    expected_output="A detailed research summary with key facts, statistics and insights.",
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
    expected_output="A review with: Quality Score (X/10), Strengths, Weaknesses, Final Verdict",
    agent=reviewer,
    context=[writing_task]
)


# Crew (Crew is the manager of agents and tasks)
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    verbose=True
)

print("\nCrew is working...\n")
result = crew.kickoff()


# print("\n" + "="*50)
# print("FINAL RESULT:")
# print("="*50)
# print(result)
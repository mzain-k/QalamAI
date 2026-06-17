import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

# ── Connect Gemini to CrewAI ──────────────────────
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# ── Create an Agent ───────────────────────────────
researcher = Agent(
    role="Research Analyst",
    goal="Research the given topic and provide a detailed, structured summary",
    backstory="""You are an expert research analyst with years of experience 
    summarizing complex topics clearly and concisely. You always structure 
    your findings with key points and conclusions.""",
    llm=llm,
    verbose=True
)

# ── Give it a Task ────────────────────────────────
topic = input("Enter a topic to research: ")

task = Task(
    description=f"Research this topic thoroughly and provide a structured summary: {topic}",
    expected_output="A structured summary with: Overview, Key Points (3-5 bullets), and Conclusion",
    agent=researcher
)

# ── Run the Crew ──────────────────────────────────
crew = Crew(
    agents=[researcher],
    tasks=[task],
    verbose=True
)

print("\nAgent is working...\n")
result = crew.kickoff()

print("\n" + "="*50)
print("FINAL RESULT:")
print("="*50)
print(result)
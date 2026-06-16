import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, LLM

load_dotenv()

# COnnect Gemini to CrewAI
llm = LLM(
    model = "gemini/gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

# Create an Agent
researcher = Agent(
    role = "Islamic Thought Leader",
    goal = "Explain Topics through fundamental Islamic Principles not the modernized version. Cover every aspect breifly. Give the proper refernces.",
    backstory = """You are a based Muslim, who is strong on his believes. 
    You are gentle to your students but you have a very hard stance when 
    it comes to the religion and specially the system and Rules that shariah 
    defines. You believe that muslim men should be strong and in a powerful position in every field specially militarily.
    You will never ever compromise Islam for anyone, even if it costs your life.""",
    llm = llm,
    verbose = True
)

# Assign a task to agent
topic = input("Enter the topic to Understand from an Islamic persective: ")

task = Task(
    description = f"Research and provide a short and concise explainantion on: {topic}",
    expected_output = "A structured explaination with bulllet point to summarize and a conclusion.",
    agent = researcher
)

# Run them with Crew (Crew is the manager of agents and tasks)
crew = Crew(
    agents = [researcher],
    tasks = [task],
    verbose = True
)

print("\n\nAgent is Working...\n")
result = crew.kickoff()

# print("\n" + "=" * 50)
# print("Final Result: ")
# print("=" * 50)
# print(result)
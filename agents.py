from crewai import Agent, LLM  # <-- Import LLM from crewai
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()

groq_llm = LLM(   #Connects to Groq
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Research Agent
blog_researcher = Agent(   #We are creating first agent.
    role="Senior YouTube Content Researcher",
    goal="Fetch transcript from YouTube video and extract key insights about {topic}",
    verbose=True,
    memory=True,   #Agent remembers previous conversation.
    backstory=(
        "You are an AI expert specializing in AI, ML, Data Science, and GenAI."
        "You analyze video transcripts deeply and extract structured insights."
    ),
    llm=groq_llm,  
    tools=[yt_tool],  #This allows agent to use your YouTube transcript tool.
    allow_delegation=True, #Research agent can give work to another agent if needed.
)

# Writer Agent   # #We are creating second agent.
blog_writer = Agent(
    role="Tech Blog Writer",
    goal="Create an engaging blog post based on transcript insights about {topic}",
    verbose=True,
    memory=True,   #Agent remembers previous conversation.
    backstory=(
        "You simplify complex AI topics into engaging and easy-to-read blog posts."
    ),
    llm=groq_llm,  
    tools=[yt_tool], #This allows agent to use your YouTube transcript tool.
    allow_delegation=False, #Research agent cannot give work to another agent if needed.
)
from crewai import Agent, LLM
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()

groq_llm = LLM(   
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


blog_researcher = Agent(  
    role="Senior YouTube Content Researcher",
    goal="Fetch transcript from YouTube video and extract key insights about {topic}",
    verbose=True,
    memory=True,   
    backstory=(
        "You are an AI expert specializing in AI, ML, Data Science, and GenAI."
        "You analyze video transcripts deeply and extract structured insights."
    ),
    llm=groq_llm,  
    tools=[yt_tool], 
    allow_delegation=True, 
)


blog_writer = Agent(
    role="Tech Blog Writer",
    goal="Create an engaging blog post based on transcript insights about {topic}",
    verbose=True,
    memory=True,   
    backstory=(
        "You simplify complex AI topics into engaging and easy-to-read blog posts."
    ),
    llm=groq_llm,  
    tools=[yt_tool],
    allow_delegation=False,
)

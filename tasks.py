from crewai import Task #We are importing Task class (to create tasks).
from agents import blog_researcher, blog_writer  # importing two agents.

# Research Task
research_task = Task(  #This creates the first task.
    description=(
        "Use the YouTube Transcript Tool to fetch transcript from this URL: {video_url}. "
        "Analyze it carefully and extract detailed insights about {topic}."
    ),
    expected_output="A detailed 3-paragraph research summary based on the transcript.",
    agent=blog_researcher,   #Research task will be done by blog_researcher agent.
)

# Writing Task
write_task = Task( ##This creates the second task.
    description=(
        "Using the research summary, create a well-structured, engaging blog post "
        "about {topic} suitable for publishing."
    ),
    expected_output="A complete blog post in markdown format.",
    agent=blog_writer,   #Writing task will be done by blog_writer agent.
    output_file="new-blog-post.md",  #After writing blog,Save it inside a file👉 File name = new-blog-post.md
)
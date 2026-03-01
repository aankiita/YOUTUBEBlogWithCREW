from crewai import Task 
from agents import blog_researcher, blog_writer  


research_task = Task(  
    description=(
        "Use the YouTube Transcript Tool to fetch transcript from this URL: {video_url}. "
        "Analyze it carefully and extract detailed insights about {topic}."
    ),
    expected_output="A detailed 3-paragraph research summary based on the transcript.",
    agent=blog_researcher,   
)


write_task = Task( 
    description=(
        "Using the research summary, create a well-structured, engaging blog post "
        "about {topic} suitable for publishing."
    ),
    expected_output="A complete blog post in markdown format.",
    agent=blog_writer,  
    output_file="new-blog-post.md",  
)

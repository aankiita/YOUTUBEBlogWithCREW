from crewai import Crew, Process 
from agents import blog_researcher, blog_writer  
from tasks import research_task, write_task  

crew = Crew(  
    agents=[blog_researcher, blog_writer],  
    tasks=[research_task, write_task],  
    process=Process.sequential, 
    memory=True, 
    cache=True, 
    max_rpm=100,
    share_crew=True, 
)

if __name__ == "__main__": 
    result = crew.kickoff(
        inputs={ 
            "topic": "AI vs ML vs DL vs Data Science",
            "video_url": "https://youtu.be/k2P_pHQDlp0?si=b0FOr1iXZ07tmAud"
        }
    )

    print("\n\nFINAL OUTPUT:\n") 
    print(result)

from crewai import Crew, Process  #Crew → Used to create a team of agents  and Process → Decides how tasks run (sequential or parallel)
from agents import blog_researcher, blog_writer  #Importing the two agents you created earlier.
from tasks import research_task, write_task  #Importing the two tasks you created.

crew = Crew(  #This creates your AI team.
    agents=[blog_researcher, blog_writer],  #So your crew has: Researcher ,Writer
    tasks=[research_task, write_task],  #So crew knows:Step 1 → Research ,Step 2 → Write
    process=Process.sequential,  #Research → then → Writing
    memory=True,  #Crew remembers previous results.
    cache=True,  #If same input is used again,  ->it may reuse previous result instead of running again.
    max_rpm=100,
    share_crew=True,  #Allows sharing crew state between tasks.
)

if __name__ == "__main__":  #Only run this code if file is executed directly -->Not when imported somewhere else
    result = crew.kickoff(
        inputs={ #  These values replace:{topic} {video_url} from tools.py,agents.py and task.py
            "topic": "AI vs ML vs DL vs Data Science",
            "video_url": "https://youtu.be/k2P_pHQDlp0?si=b0FOr1iXZ07tmAud"
        }
    )

    print("\n\nFINAL OUTPUT:\n")  #This prints final result in terminal.
    print(result)
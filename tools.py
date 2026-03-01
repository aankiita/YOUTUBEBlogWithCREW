from crewai.tools import BaseTool  #This imports BaseTool from CrewAI.Any tool you create in CrewAI must inherit from BaseTool.
from langchain_community.document_loaders import YoutubeLoader  #This imports a tool that can fetch YouTube subtitle.It returns subtitle as text.

class YouTubeTranscriptTool(BaseTool): #We are creating a new tool class.It inherit the baseTool.
    name: str = "youtube_transcript_tool" #This is the tool's name (in string)
    description: str = "Fetch transcript content from a YouTube video URL"  #This tells the agent what the tool does.The LLM reads this description to decide when to use the tool.

    def _run(self, video_url: str):   #Whenever agent calls this tool, this function runs.
        loader = YoutubeLoader.from_youtube_url(  #load the youtube URL
            video_url,
            add_video_info=True  #also it has youtube video all information.
        )
        docs = loader.load() #This actually fetches subtitle from YouTube, and return it as list of documents.

        if not docs:
            return "No transcript found."

        return docs[0].page_content

yt_tool = YouTubeTranscriptTool()  #This creates an object of the class.-->Now we can pass it into agents:
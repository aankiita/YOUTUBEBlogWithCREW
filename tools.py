from crewai.tools import BaseTool  
from langchain_community.document_loaders import YoutubeLoader 

class YouTubeTranscriptTool(BaseTool):
    name: str = "youtube_transcript_tool" 
    description: str = "Fetch transcript content from a YouTube video URL" 

    def _run(self, video_url: str):  
        loader = YoutubeLoader.from_youtube_url( 
            video_url,
            add_video_info=True  
        docs = loader.load() 

        if not docs:
            return "No transcript found."

        return docs[0].page_content

yt_tool = YouTubeTranscriptTool()  

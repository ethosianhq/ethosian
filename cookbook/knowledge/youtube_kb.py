import os
from os import getenv
from ethosian.agent import Agent
from ethosian.knowledge.youtube import YouTubeKnowledgeBase, YouTubeReader
from ethosian.vectordb.qdrant import Qdrant

api_key = getenv("QDRANT_API_KEY")
qdrant_url = getenv("QDRANT_URL")

vector_db = Qdrant(collection="youtube-ethosian",
                   url=qdrant_url, api_key=api_key)

os.environ["OPENAI_API_KEY"] = "<replace-with-openai-key>"

# Create a knowledge base with the PDFs from the data/pdfs directory
knowledge_base = YouTubeKnowledgeBase(
    urls=["https://www.youtube.com/watch?v=CDC3GOuJyZ0"],
    vector_db=vector_db,
    reader=YouTubeReader(chunk=True),
)
# only once, comment it out after first run
knowledge_base.load(recreate=False)

agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

agent.print_response(
    "what is the major focus of the knowledge provided?", markdown=True)

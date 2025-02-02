# install chromadb - `pip install chromadb`

from ethosian.agent import Agent
from ethosian.knowledge.pdf import PDFUrlKnowledgeBase
from ethosian.vectordb.chroma import ChromaDb

# Initialize ChromaDB
vector_db = ChromaDb(collection="recipes",
                     path="tmp/chromadb", persistent_client=True)

# Create knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://ethosian-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_base.load(recreate=False)  # Comment out after first run

# Create and use the agent
agent = Agent(knowledge_base=knowledge_base,
              use_tools=True, show_tool_calls=True)
agent.print_response("Show me how to make Tom Kha Gai", markdown=True)

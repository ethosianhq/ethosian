from ethosian.agent import Agent
from ethosian.knowledge.pdf import PDFUrlKnowledgeBase
from ethosian.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://ethosian-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(knowledge_base=knowledge_base,
              use_tools=True, show_tool_calls=True)
agent.print_response("How to make Thai curry?", markdown=True)

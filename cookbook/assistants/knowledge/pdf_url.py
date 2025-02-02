from ethosian.assistant import Assistant
from ethosian.knowledge.pdf import PDFUrlKnowledgeBase
from ethosian.vectordb.pgvector import PgVector2

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://ethosian-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes", db_url=db_url),
)
knowledge_base.load(recreate=False)  # Comment out after first run

assistant = Assistant(knowledge_base=knowledge_base,
                      use_tools=True, show_tool_calls=True)
assistant.print_response("How to make Thai curry?", markdown=True)

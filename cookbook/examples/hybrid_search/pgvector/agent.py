from ethosian.agent import Agent
from ethosian.model.openai import OpenAIChat
from ethosian.knowledge.pdf import PDFUrlKnowledgeBase
from ethosian.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://ethosian-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url,
                       search_type=SearchType.hybrid),
)
# Load the knowledge base: Comment out after first run
knowledge_base.load(upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
)
agent.print_response(
    "How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What was my last question?", stream=True)

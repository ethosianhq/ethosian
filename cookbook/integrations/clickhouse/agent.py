from ethosian.agent import Agent
from ethosian.knowledge.pdf import PDFUrlKnowledgeBase
from ethosian.storage.agent.sqlite import SqlAgentStorage
from ethosian.vectordb.clickhouse import ClickhouseDb

agent = Agent(
    storage=SqlAgentStorage(table_name="recipe_agent"),
    knowledge_base=PDFUrlKnowledgeBase(
        urls=["https://ethosian-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=ClickhouseDb(
            table_name="recipe_documents",
            host="localhost",
            port=8123,
            username="ai",
            password="ai",
        ),
    ),
    # Show tool calls in the response
    show_tool_calls=True,
    # Enable the agent to search the knowledge base
    search_knowledge=True,
    # Enable the agent to read the chat history
    read_chat_history=True,
)
# Comment out after first run
agent.knowledge.load(recreate=False)  # type: ignore

agent.print_response("How do I make pad thai?", markdown=True)

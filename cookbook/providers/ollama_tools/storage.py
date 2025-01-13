"""Run `pip install duckduckgo-search sqlalchemy ollama` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.ollama import OllamaTools
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.storage.agent.postgres import PgAgentStorage

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=OllamaTools(id="llama3.1:8b"),
    storage=PgAgentStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGo()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")

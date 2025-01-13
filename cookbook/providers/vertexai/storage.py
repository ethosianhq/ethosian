"""Run `pip install duckduckgo-search sqlalchemy google.generativeai` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.vertexai import Gemini
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.storage.agent.postgres import PgAgentStorage

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    storage=PgAgentStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGo()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")

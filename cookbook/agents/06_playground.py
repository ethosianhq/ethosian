"""Run `pip install openai yfinance duckduckgo-search ethosian 'fastapi[standard]' sqlalchemy` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.openai import OpenAIChat
from ethosian.storage.agent.sqlite import SqlAgentStorage
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.tools.yfinance import YFinanceTools
from ethosian.playground import Playground, serve_playground_app

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(enable_all=True)],
    instructions=["Use tables to display data"],
    # Add long-term memory to the agent
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    # Add history from long-term memory to the agent's messages
    add_history_to_messages=True,
    markdown=True,
)

app = Playground(agents=[finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("06_playground:app", reload=True)

from ethosian.agent import Agent
from ethosian.model.openai import OpenAIChat
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.tools.yfinance import YFinanceTools
from ethosian.storage.agent.sqlite import SqlAgentStorage
from ethosian.playground import Playground, serve_playground_app

web_agent = Agent(
    name="Web Agent",
    agent_id="web_agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(
        table_name="web_agent_sessions", db_file="tmp/agents.db"),
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    agent_id="finance_agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqlAgentStorage(
        table_name="finance_agent_sessions", db_file="tmp/agents.db"),
    markdown=True,
)

agent_team = Agent(
    name="Agent Team",
    agent_id="agent_team",
    team=[web_agent, finance_agent],
    storage=SqlAgentStorage(
        table_name="agent_team_sessions", db_file="tmp/agents.db"),
    markdown=True,
)

app = Playground(agents=[finance_agent, web_agent, agent_team]).get_app()

if __name__ == "__main__":
    serve_playground_app("04_agent_ui:app", reload=True)

"""Run `pip install openai yfinance ethosian` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.openai import OpenAIChat
from ethosian.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent.print_response(
    "Summarize and compare analyst recommendations for NVDA for TSLA", stream=True)

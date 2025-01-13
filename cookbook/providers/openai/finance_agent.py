"""Run `pip install yfinance` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.openai import OpenAIChat
from ethosian.tools.yfinance import YFinanceTools

finance_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(
        stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent.print_response(
    "Summarize and compare analyst recommendations for NVDA for TSLA", stream=True)

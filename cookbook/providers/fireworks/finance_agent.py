"""Run `pip install yfinance` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.fireworks import Fireworks
from ethosian.tools.yfinance import YFinanceTools

agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/firefunction-v2"),
    tools=[YFinanceTools(
        stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
)

# agent.print_response("Share the NVDA stock price and analyst recommendations", stream=True)
agent.print_response("Summarize fundamentals for TSLA", stream=True)

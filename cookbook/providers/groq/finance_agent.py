"""Run `pip install yfinance` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.groq import Groq
from ethosian.tools.yfinance import YFinanceTools

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA. Show in tables.", stream=True
)

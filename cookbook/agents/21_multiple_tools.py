"""Run `pip install openai duckduckgo-search yfinance` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.openai import OpenAIChat
from ethosian.tools.yfinance import YFinanceTools
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo(), YFinanceTools(enable_all=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response(
    "Write a thorough report on NVDA, get all financial information and latest news", stream=True)

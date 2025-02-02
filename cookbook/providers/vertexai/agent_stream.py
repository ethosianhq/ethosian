"""Run `pip install yfinance` to install dependencies."""

from typing import Iterator  # noqa
from ethosian.agent import Agent, RunResponse  # noqa
from ethosian.model.vertexai import Gemini
from ethosian.tools.yfinance import YFinanceTools

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[YFinanceTools(stock_price=True)],
    instructions=["Use tables where possible."],
    markdown=True,
    show_tool_calls=True,
)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("What is the stock price of NVDA and TSLA", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
agent.print_response("What is the stock price of NVDA and TSLA", stream=True)

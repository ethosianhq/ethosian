"""Run `pip install yfinance` to install dependencies."""

from ethosian.agent import Agent, RunResponse  # noqa
from ethosian.model.ollama import OllamaTools
from ethosian.tools.yfinance import YFinanceTools

agent = Agent(
    model=OllamaTools(id="llama3.1:8b"),
    tools=[YFinanceTools(stock_price=True)],
    show_tool_calls=True,
    markdown=True,
)

# Get the response in a variable
# run: RunResponse = agent.run("What is the stock price of NVDA and TSLA")
# print(run.content)

# Print the response in the terminal
agent.print_response("What is the stock price of NVDA and TSLA")

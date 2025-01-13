"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.anthropic import Claude
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(model=Claude(id="claude-3-5-sonnet-20240620"),
              tools=[DuckDuckGo()], show_tool_calls=True, markdown=True)
agent.print_response("Whats happening in France?", stream=True)

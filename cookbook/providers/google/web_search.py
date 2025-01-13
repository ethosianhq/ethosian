"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.google import Gemini
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(model=Gemini(id="gemini-2.0-flash-exp"),
              tools=[DuckDuckGo()], show_tool_calls=True, markdown=True)
agent.print_response("Whats happening in France?", stream=True)

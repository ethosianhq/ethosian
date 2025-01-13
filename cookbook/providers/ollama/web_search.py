"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.ollama import Ollama
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(model=Ollama(id="llama3.1:8b"), tools=[
              DuckDuckGo()], show_tool_calls=True, markdown=True)
agent.print_response("Whats happening in France?", stream=True)

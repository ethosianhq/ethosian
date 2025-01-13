"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.together import Together
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)

"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.cohere import CohereChat
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=CohereChat(id="command-r-08-2024"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)

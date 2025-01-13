"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.azure import AzureOpenAIChat
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=AzureOpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)

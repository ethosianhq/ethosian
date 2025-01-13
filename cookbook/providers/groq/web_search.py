"""Run `pip install duckduckgo-search` to install dependencies."""

from ethosian.agent import Agent
from ethosian.model.groq import Groq
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)

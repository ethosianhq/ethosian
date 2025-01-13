from ethosian.agent import Agent
from ethosian.model.anthropic import Claude
from ethosian.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    tools=[DuckDuckGo()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and search the web for more information.",
    images=[
        "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
    ],
    stream=True,
)

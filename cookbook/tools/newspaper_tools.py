from ethosian.agent import Agent
from ethosian.tools.newspaper_tools import NewspaperTools

agent = Agent(tools=[NewspaperTools()])
agent.print_response(
    "Please summarize https://en.wikipedia.org/wiki/Language_model")

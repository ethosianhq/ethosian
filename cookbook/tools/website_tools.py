from ethosian.agent import Agent
from ethosian.tools.website import WebsiteTools

agent = Agent(tools=[WebsiteTools()], show_tool_calls=True)
agent.print_response(
    "Search web page: 'https://docs.ethosianhq.com/introduction'", markdown=True)

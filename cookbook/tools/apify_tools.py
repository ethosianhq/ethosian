from ethosian.agent import Agent
from ethosian.tools.apify import ApifyTools

agent = Agent(tools=[ApifyTools()], show_tool_calls=True)
agent.print_response(
    "Tell me about https://docs.ethosianhq.com/introduction", markdown=True)

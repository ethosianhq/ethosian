from ethosian.agent import Agent
from ethosian.tools.serpapi_tools import SerpApiTools

agent = Agent(tools=[SerpApiTools()], show_tool_calls=True)
agent.print_response("Whats happening in the USA?", markdown=True)

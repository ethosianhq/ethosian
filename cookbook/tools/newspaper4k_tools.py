from ethosian.agent import Agent
from ethosian.tools.newspaper4k import Newspaper4k

agent = Agent(tools=[Newspaper4k()], debug_mode=True, show_tool_calls=True)
agent.print_response(
    "Please summarize https://www.rockymountaineer.com/blog/experience-icefields-parkway-scenic-drive-lifetime"
)

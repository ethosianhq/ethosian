from ethosian.agent import Agent
from ethosian.tools.jina_tools import JinaReaderTools

agent = Agent(tools=[JinaReaderTools()], debug_mode=True, show_tool_calls=True)
agent.print_response("Summarize: https://github.com/ethosianhq")

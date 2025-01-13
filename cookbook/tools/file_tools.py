from ethosian.agent import Agent
from ethosian.tools.file import FileTools

agent = Agent(tools=[FileTools()], show_tool_calls=True)
agent.print_response(
    "What is the most advanced LLM currently? Save the answer to a file.", markdown=True)

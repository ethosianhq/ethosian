"""Run `pip install duckduckgo-search openai` to install dependencies."""

from ethosian.agent import Agent
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.storage.agent.yaml import YamlFileAgentStorage

agent = Agent(
    storage=YamlFileAgentStorage(dir_path="tmp/agent_sessions_yaml"),
    tools=[DuckDuckGo()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")

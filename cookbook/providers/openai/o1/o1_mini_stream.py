from typing import Iterator  # noqa
from ethosian.agent import Agent, RunResponse  # noqa
from ethosian.model.openai import OpenAIChat

agent = Agent(model=OpenAIChat(id="o1-mini"))

# Print the response in the terminal
agent.print_response("What is the closest galaxy to milky way?", stream=True)

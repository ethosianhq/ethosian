from ethosian.agent import Agent, RunResponse  # noqa
from ethosian.model.fireworks import Fireworks

agent = Agent(model=Fireworks(
    id="accounts/fireworks/models/firefunction-v2"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")

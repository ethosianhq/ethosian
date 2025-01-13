from ethosian.agent import Agent
from ethosian.tools.ethosian import ethosianTools

# Create an Agent with the ethosian tool
agent = Agent(tools=[ethosianTools()], name="ethosian Workspace Manager")

# Example 1: Create a new agent app
agent.print_response(
    "Create a new agent-app called agent-app-turing", markdown=True)

# Example 3: Start a workspace
agent.print_response("Start the workspace agent-app-turing", markdown=True)

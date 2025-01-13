from ethosian.agent import Agent
from composio_ethosian import Action, ComposioToolSet  # type: ignore

toolset = ComposioToolSet()
composio_tools = toolset.get_tools(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER])

agent = Agent(tools=composio_tools, show_tool_calls=True)
agent.print_response("Can you star ethosianhq/ethosian repo?")

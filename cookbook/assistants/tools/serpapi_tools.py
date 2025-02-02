from ethosian.assistant import Assistant
from ethosian.tools.serpapi_tools import SerpApiTools

assistant = Assistant(
    tools=[SerpApiTools()],
    show_tool_calls=True,
    debug_mode=True,
)

assistant.print_response("Whats happening in the USA?", markdown=True)

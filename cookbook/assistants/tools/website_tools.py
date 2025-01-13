from ethosian.assistant import Assistant
from ethosian.tools.website import WebsiteTools

assistant = Assistant(tools=[WebsiteTools()], show_tool_calls=True)
assistant.print_response(
    "Search web page: 'https://docs.ethosianhq.com/introduction'", markdown=True)

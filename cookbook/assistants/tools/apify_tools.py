from ethosian.assistant import Assistant
from ethosian.tools.apify import ApifyTools

assistant = Assistant(tools=[ApifyTools()], show_tool_calls=True)
assistant.print_response(
    "Tell me about https://docs.ethosianhq.com/introduction", markdown=True)

from ethosian.assistant import Assistant
from ethosian.tools.duckduckgo import DuckDuckGo

assistant = Assistant(tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response(
    "Give me news from 3 different countries.", markdown=True)

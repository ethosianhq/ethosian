from ethosian.assistant import Assistant
from ethosian.tools.wikipedia import WikipediaTools

assistant = Assistant(tools=[WikipediaTools()], show_tool_calls=True)
assistant.print_response("Search wikipedia for 'ai'", markdown=True)

from ethosian.assistant import Assistant
from ethosian.tools.tavily import TavilyTools

assistant = Assistant(tools=[TavilyTools()], show_tool_calls=True)
assistant.print_response("Search tavily for 'language models'", markdown=True)

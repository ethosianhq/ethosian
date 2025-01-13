from ethosian.assistant import Assistant
from ethosian.llm.google import Gemini
from ethosian.tools.duckduckgo import DuckDuckGo

assistant = Assistant(llm=Gemini(model="gemini-1.5-flash"),
                      tools=[DuckDuckGo()], debug_mode=True, show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)

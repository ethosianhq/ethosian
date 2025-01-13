from ethosian.assistant import Assistant
from ethosian.llm.openai import OpenAIChat
from ethosian.tools.duckduckgo import DuckDuckGo


assistant = Assistant(llm=OpenAIChat(model="gpt-4-turbo"),
                      tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)

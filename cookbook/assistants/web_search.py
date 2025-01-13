from ethosian.assistant import Assistant
from ethosian.llm.openai import OpenAIChat
from ethosian.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response(
    "Search for news from France and write a short poem about it.")

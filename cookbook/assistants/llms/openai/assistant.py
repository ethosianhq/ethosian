from ethosian.assistant import Assistant
from ethosian.llm.openai import OpenAIChat
from ethosian.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o", max_tokens=500, temperature=0.3),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)
assistant.print_response("Whats happening in France?", markdown=True)

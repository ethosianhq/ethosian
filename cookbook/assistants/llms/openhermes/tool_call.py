from ethosian.assistant import Assistant
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.llm.ollama import Ollama

assistant = Assistant(
    llm=Ollama(model="openhermes"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    # debug_mode=True
)
assistant.print_response("Tell me about OpenAI Sora", markdown=True)

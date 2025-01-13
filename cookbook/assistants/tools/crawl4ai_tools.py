from ethosian.assistant import Assistant
from ethosian.tools.crawl4ai_tools import Crawl4aiTools

assistant = Assistant(tools=[Crawl4aiTools(
    max_length=None)], show_tool_calls=True)
assistant.print_response(
    "Tell me about https://github.com/ethosianhq/ethosian.", markdown=True)

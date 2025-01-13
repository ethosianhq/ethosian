# pip install firecrawl-py openai

import os

from ethosian.assistant import Assistant
from ethosian.tools.firecrawl import FirecrawlTools

api_key = os.getenv("FIRECRAWL_API_KEY")

assistant = Assistant(
    tools=[FirecrawlTools(api_key=api_key, scrape=False, crawl=True)], show_tool_calls=True, markdown=True
)
assistant.print_response("summarize this https://finance.yahoo.com/")

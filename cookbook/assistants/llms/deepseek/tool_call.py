from ethosian.assistant import Assistant
from ethosian.llm.deepseek import DeepSeekChat
from ethosian.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=DeepSeekChat(),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response(
    "Write a comparison between NVDA and AMD, use all tools available.")

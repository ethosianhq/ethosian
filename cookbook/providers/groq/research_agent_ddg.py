"""Please install dependencies using:
pip install openai duckduckgo-search newspaper4k lxml_html_clean ethosian
"""

from ethosian.agent import Agent
from ethosian.model.groq import Groq
from ethosian.tools.duckduckgo import DuckDuckGo
from ethosian.tools.newspaper4k import Newspaper4k

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    # debug_mode=True,
)
agent.print_response("Simulation theory", stream=True)

from ethosian.assistant import Assistant
from ethosian.tools.duckdb import DuckDbTools

assistant = Assistant(
    tools=[DuckDbTools()],
    show_tool_calls=True,
    system_prompt="Use this file for Movies data: https://ethosian-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
)
assistant.print_response(
    "What is the average rating of movies?", markdown=True, stream=False)

import json

from ethosian.assistant.duckdb import DuckDbAssistant
from ethosian.llm.fireworks import Fireworks

duckdb_assistant = DuckDbAssistant(
    llm=Fireworks(),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "https://ethosian-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        }
    ),
    show_tool_calls=True,
    # debug_mode=True,
)

duckdb_assistant.print_response(
    "What is the average rating of movies? Show me the SQL.", markdown=True)

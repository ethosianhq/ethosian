from ethosian.llm.groq import Groq
from ethosian.assistant.duckdb import DuckDbAssistant

data_analyst = DuckDbAssistant(
    llm=Groq(model="llama3-70b-8192"),
    semantic_model="""
    tables:
      - name: movies
        description: "Contains information about movies from IMDB."
        path: "https://ethosian-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"
    """,
    show_tool_calls=True,
)
data_analyst.cli_app(markdown=True, stream=False, user="Groq")

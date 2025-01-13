from ethosian.assistant import Assistant
from ethosian.tools.sql import SQLTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

assistant = Assistant(
    tools=[
        SQLTools(
            db_url=db_url,
        )
    ],
    show_tool_calls=True,
)

assistant.print_response(
    "List the tables in the database. Tell me about contents of one of the tables", markdown=True)

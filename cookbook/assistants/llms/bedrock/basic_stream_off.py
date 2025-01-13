from ethosian.assistant import Assistant
from ethosian.llm.aws.claude import Claude

assistant = Assistant(
    llm=Claude(model="anthropic.claude-3-5-sonnet-20240620-v1:0"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a quick healthy breakfast recipe.", markdown=True, stream=False)

import os

from ethosian.assistant import Assistant
from ethosian.llm.mistral import MistralChat

assistant = Assistant(
    llm=MistralChat(
        model="mistral-large-latest",
        api_key=os.environ["MISTRAL_API_KEY"],
    ),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a quick healthy breakfast recipe.", markdown=True, stream=False)

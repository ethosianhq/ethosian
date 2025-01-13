from ethosian.assistant import Assistant
from ethosian.llm.openai.like import OpenAILike

assistant = Assistant(llm=OpenAILike(base_url="http://localhost:1234/v1"))
assistant.print_response(
    "Share a quick healthy breakfast recipe.", stream=False, markdown=True)

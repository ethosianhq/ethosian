# Please install dependencies using: pip install -U ollama ethosian openai
from ethosian.assistant import Assistant
from ethosian.llm.ollama.openai import OllamaOpenAI

assistant = Assistant(
    llm=OllamaOpenAI(model="tinyllama"),
    system_prompt="Who are you and who created you? Respond in 1 sentence.",
)
assistant.print_response(markdown=True)

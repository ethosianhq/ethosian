from ethosian.assistant import Assistant
from ethosian.llm.groq import Groq
from ethosian.tools.calculator import Calculator

assistant = Assistant(
    llm=Groq(model="llama-3.1-405b-reasoning"),
    tools=[Calculator(add=True, subtract=True, multiply=True, divide=True)],
    instructions=["Use the calculator tool for comparisons."],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("Is 9.11 bigger than 9.9?")
assistant.print_response("9.11 and 9.9 -- which is bigger?")

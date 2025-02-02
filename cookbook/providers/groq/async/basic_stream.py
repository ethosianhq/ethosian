import asyncio
from ethosian.agent import Agent
from ethosian.model.groq import Groq

assistant = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)
# -*- Print a response to the cli
asyncio.run(assistant.aprint_response(
    "Share a breakfast recipe.", markdown=True, stream=True))

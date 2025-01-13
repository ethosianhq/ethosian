from ethosian.assistant import Assistant
from ethosian.llm.openai import OpenAIChat
from ethosian.utils.log import logger

assistant = Assistant(llm=OpenAIChat(model="gpt-4o"))
# -*- Print a response to the cli
assistant.print_response("Share a 1 line joke")

# -*- Print the assistant memory
logger.info("*** Assistant Memory ***")
logger.info(assistant.memory.to_dict())

# -*- Clear the assistant memory
logger.info("Clearing the assistant memory...")
assistant.memory.clear()
logger.info("*** Assistant Memory ***")
logger.info(assistant.memory.to_dict())

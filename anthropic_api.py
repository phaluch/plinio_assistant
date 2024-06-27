from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620", name="Banana_Model")

messages = [
    SystemMessage(
        content="You are a funny assistant, that always makes jokes involving bananas.",
        name="Banana_Assistant",
    ),
    HumanMessage(
        content="What weigths more, a kilo of lead or a kilo of cotton?", name="Human"
    ),
]

result = model.invoke(messages)

print(result)

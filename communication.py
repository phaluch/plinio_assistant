# Creating the first version of a graph to check the communication

from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
from pprint import pprint

from state import AgentState

load_dotenv()


# Functions that'll invoke each agent and handle the state
def human_interface(state):
    model = ChatOpenAI(model="gpt-4o")
    human_input = input("Human: ")
    messages = [
        SystemMessage(
            content="You are a funny assistant, that always makes jokes involving bananas.",
            name="BananaSystem",
        ),
        HumanMessage(
            content=human_input,
            name="Human",
        ),
    ]
    state.messages.extend(messages)
    print("HI: Number of messages:", len(state.messages))
    result = model.invoke(state.messages)
    result_message = HumanMessage(content=result.content, name="BananaAssistant")
    return {"messages": [result_message]}


def joke_analyzer(state):
    model = ChatOpenAI(model="gpt-4o")
    messages = [
        SystemMessage(
            content="You are a jokes specialist, that analyzes jokes in excruciating detail.",
            name="JokeSystem",
        ),
    ]
    state.messages.extend(messages)
    print("JA: Number of messages:", len(state.messages))
    result = model.invoke(state.messages)
    result_message = AIMessage(content=result.content, name="JokeAssistant")
    return {"messages": [result_message]}


workflow = StateGraph(AgentState)

workflow.add_node("human_interface", human_interface)
workflow.add_node("joke_analyzer", joke_analyzer)

workflow.add_edge("human_interface", "joke_analyzer")
workflow.set_entry_point("human_interface")


app = workflow.compile()

state = AgentState(messages=[])

result = app.invoke(state)
"""
for s in app.stream(state):
    if "__end__" not in s:
        print(s)
        print("----")
"""
print(30 * "#")
pprint(result)

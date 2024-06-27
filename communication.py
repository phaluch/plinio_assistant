# Creating the first version of a graph to check the communication

from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from state import State
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

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

    result = model.invoke(messages)
    result_message = AIMessage(content=result.content, name="BananaAssistant")
    state.messages.append(result_message)
    return state


def joke_analyzer(state):
    model = ChatOpenAI(model="gpt-4o")
    messages = [
        SystemMessage(
            content="You are a jokes specialist, that analyzes jokes in excruciating detail.",
            name="JokeSystem",
        ),
    ]
    state.messages.extend(messages)

    result = model.invoke(state.messages)
    result_message = AIMessage(content=result.content, name="JokeAssistant")
    state.messages.append(result_message)
    return state


workflow = StateGraph(State)

workflow.add_node("human_interface", human_interface)
workflow.add_node("joke_analyzer", joke_analyzer)

workflow.add_edge("human_interface", "joke_analyzer")
workflow.set_entry_point("human_interface")

state = State()

app = workflow.compile()
app.invoke(state)
print(state)

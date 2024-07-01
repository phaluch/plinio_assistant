# Definir um nó
# Adicionar o nó ao grafo

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph
import operator
from typing import Sequence, TypedDict


# Functions that'll invoke each agent and handle the state
def square(x):
    """
    Squares the value of the given state.

    Parameters:
    state (object): The state object containing the value to be squared.

    Returns:
    object: The updated state object with the squared value.
    """
    x = x**2
    return x


# The agent state is the input to each node in the graph
class AgentState(TypedDict):
    # The annotation tells the graph that new messages will always
    # be added to the current states
    messages: Annotated[Sequence[str], operator.add]


workflow = StateGraph(AgentState)

workflow.add_node("square", square)

workflow.set_entry_point("square")
app = workflow.compile()
for s in app.stream(3):
    print(list(s.values())[0])
    print("----")

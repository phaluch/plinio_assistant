import operator
from typing import Annotated, Sequence

from langchain_core.messages import BaseMessage
from langchain_core.pydantic_v1 import BaseModel


class AgentState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], operator.add]

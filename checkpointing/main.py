# Checkpointing in LangGraph is the process of saving a graph's execution state after each step.
# It allows workflows to resume from the last saved point, supports persistent memory,
# fault tolerance, conversation history, and human-in-the-loop interactions.
# Checkpoints are typically stored using MemorySaver, SQLite, or PostgreSQL-based checkpointers.

from typing import  TypedDict,Annotated

from langchain_protocol import Checkpoint
from langgraph.graph import START, StateGraph,END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage,AIMessage
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list,add_messages]


def chat(state:State):
    return {"messages":[AIMessage(content="hi hello there")]}

graphBuilder=StateGraph(State)


graphBuilder.add_node("chat",chat)
graphBuilder.add_edge(START, "chat")
graphBuilder.add_edge("chat", END)


# Checkpointer
memory=MemorySaver()
graph=graphBuilder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "user123"
    }
}


graph.invoke({"messages":[HumanMessage(content="hi")] }, config=config)

# Check saved state
state=graph.get_state(config)

for message in state.values["messages"]:
    print(message.content)











# Without Checkpointing
# Node A runs ✅
# Node B runs ✅
# Node C runs ❌ (server crashes)
# When you restart, you must start again from Node A.

# With Checkpointing
# Node A runs ✅ → state saved
# Node B runs ✅ → state saved
# Node C runs ❌ (server crashes)
# When you restart, LangGraph loads the latest checkpoint and continues from Node C instead of rerunning A and B.
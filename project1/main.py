from typing import TypedDict, Optional
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    user_query: str
    output: Optional[str]


def chat(state: State):
    print("Node Executed")
    return {"output": f"You said: {state['user_query']}"}


graph = StateGraph(State)

graph.add_node("chat", chat)

graph.add_edge(START, "chat")
graph.add_edge("chat", END)

app = graph.compile()

result = app.invoke({
    "user_query": "Hello"
})

print(result)
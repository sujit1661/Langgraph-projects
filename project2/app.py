from dotenv import load_dotenv
load_dotenv()
from groq import Groq
from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage,AIMessage
from langgraph.graph import START,StateGraph,END


llm=Groq(api_key="")

class State(TypedDict):
    messages: Annotated[list,add_messages]


def initialization(state:State):
    print("Initializing State.....")
    return state


def chat(state:State):
    last_message=state["messages"][-1].content
    response=llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role":"user","content":last_message}]
    )

    result=response.choices[0].message.content
    return {"messages":[AIMessage(content=result)]}




graphBuilder=StateGraph(State)

graphBuilder.add_node("sample",initialization)
graphBuilder.add_node("chat",chat)


graphBuilder.add_edge(START,"sample")
graphBuilder.add_edge("sample","chat")
graphBuilder.add_edge("chat",END)

graph=graphBuilder.compile()

result=graph.invoke({"messages":[HumanMessage(content="hi there")]})
print(result)



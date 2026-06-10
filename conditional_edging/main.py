from typing import TypedDict,Optional,Literal
from langgraph.graph import START, StateGraph,END
from groq import Groq

llm=Groq(api_key="")


class State(TypedDict):
    user:str
    output:Optional[str]
    is_ok:Optional[bool]


def sample(state:State):
    print("initializing the AI.....")
    return state

# model 1 to solve user query
def model1(state:State):
    print("model1 thinking,,,,,,,,,,,,")
    content=state.get("user")
    res=llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content":content }],
        max_tokens=200,
        max_completion_tokens=300
    )

    result=res.choices[0].message.content
    state["output"]=result
    return state


# basic conditional edge handling
def evaluate_result(state:State)-> Literal["model2", "endnode"]:
    if False:
        return "endnode"

    return "model2"


def endnode(state:State):
    return state

# model 2 to improve result
def model2(state:State):
    print("model2 thinking,,,,,,,,,,,,")
    content=state.get("user")
    res=llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content":content }],
        temperature=0.2,
        max_tokens=100,
        max_completion_tokens=500
    )
    result=res.choices[0].message.content
    state["output"]=result
    return state


graphBuilder=StateGraph(State)

graphBuilder.add_node("sample",sample)
graphBuilder.add_node("model1",model1)
graphBuilder.add_node("endnode",endnode)
graphBuilder.add_node("check",evaluate_result)
graphBuilder.add_node("model2",model2)


graphBuilder.add_edge(START,"sample")
graphBuilder.add_edge("sample","model1")
graphBuilder.add_conditional_edges("model1",evaluate_result)

graphBuilder.add_edge("model2","endnode")
graphBuilder.add_edge("endnode",END)



graph=graphBuilder.compile()

result=graph.invoke(State({"user":"hi there what is ci/cd"}))

print(result)


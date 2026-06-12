from groq import Groq
from neo4j import GraphDatabase
import os
from mem0 import Memory
from dotenv import load_dotenv
load_dotenv()


# groq config
llm=Groq(api_key=os.getenv("GROQ_API_KEY"))

USER_ID="sujit"

# memory
memory = Memory.from_config({
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": os.getenv("NEO4J_URI"),
            "username": os.getenv("NEO4J_USERNAME"),
            "password": os.getenv("NEO4J_PASSWORD"),
        }
    },
    "llm": {
        "provider": "groq",
        "config": {
            "api_key": os.getenv("GROQ_API_KEY"),
            "model": "openai/gpt-oss-120b"
        }
    },
    "embedder": {
            "provider": "huggingface",
            "config": {
                "model": "sentence-transformers/all-MiniLM-L6-v2"
            }
        }
})


while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    # 1. retrieve relevant memory automatically
    memories=memory.search(user_input,user_id=USER_ID)

    memory_context="\n".join([m["memory"] for m in memories])

    # 2. generate response with Groq
    messages = [
        {
            "role": "system",
            "content": f"You are a helpful assistant.\nUser memory:\n{memory_context}"
        },
        {"role": "user", "content": user_input}
    ]


    response=llm.chat.completions.create(
        messages=messages,
        model="openai/gpt-oss-120b",
    )

    reply = response.choices[0].message.content
    print("\nBot:", reply)

    # 3. automatically store memory (NO manual extraction code)
    memory.add(
        messages=[{"role": "user", "content": user_input}],
        user_id=USER_ID
    )






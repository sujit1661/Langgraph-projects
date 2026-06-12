import os
from groq import Groq
from mem0 import Memory
from qdrant_client import QdrantClient
from qdrant_client.http.models import PayloadSchemaType
from dotenv import load_dotenv
load_dotenv()


# need to make some configurations cause the default one is openai which is paid one
config={
    "vector_store":{
        "provider":"qdrant",
        "config":{
            "url":os.getenv("QDRANT_URL"),
            "api_key":os.getenv("QDRANT_API_KEY"),
            "collection_name":"chat_memory"
        }
    },
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    },

    "llm": {
        "provider": "groq",
        "config": {
            "api_key": os.getenv("GROQ_API_KEY"),
            "model": "openai/gpt-oss-120b",
        }
}


}


memory=Memory.from_config(config)

llm=Groq(api_key=os.getenv("GROQ_API_KEY"))

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

client.create_payload_index(
    collection_name="chat_memory",
    field_name="user_id",
    field_schema=PayloadSchemaType.KEYWORD
)
print(client.get_collections())

USER_ID = "user_123"


while True:
    user=input("Enter your query: ")

    if user == "exit":
        break

    memories=memory.search(query=user,user_id=USER_ID)

    memory_context = "\n".join([m["memory"] for m in memories["results"]])

    prompt = f"""
    Previous Memories:
    {memory_context}

    Current User Message:
    {user}
    """

    response=llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    assistant_reply=response.choices[0].message.content
    print(f"\nBot: {assistant_reply}")

    memory.add(
        [
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant_reply}
        ],
        user_id=USER_ID
    )
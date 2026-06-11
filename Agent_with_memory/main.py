# Mem0 is a memory layer for AI applications and agents.
# Instead of making the LLM remember everything from the current chat session only,
# Mem0 stores important information from past conversations and retrieves it when needed.




# Mem0 doesn't blindly store the message. Instead, it sends the conversation to an LLM with instructions similar to:
#
    # Analyze this conversation.
    # Extract important facts, preferences,
    # personal details, goals, and relationships.
    # Ignore greetings, small talk, and temporary information.



# Mem0 uses an LLM-based memory extraction step. Instead of storing every message,
# it analyzes conversations to identify important long-term information such as user preferences,
# personal details, goals, and relationships. It then stores only those extracted memories and ignores
# short-term or irrelevant messages like greetings and acknowledgments.


from mem0 import MemoryClient
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

memory = MemoryClient(
    api_key=os.getenv("MEM0_API_KEY")
)

llm = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

USER_ID = "sujit"

while True:
    user = input("Enter your query: ")

    if user.lower() == "exit":
        break

    # Retrieve memories
    memories = memory.search(
        query=user,
        user_id=USER_ID
    )

    memory_context = ""

    if memories:
        try:
            memory_context = "\n".join(m["memory"] for m in memories)
        except:
            try:
                memory_context = "\n".join(m.memory for m in memories)
            except:
                memory_context = ""

    messages = [{"role": "system","content": f"You are a helpful assistant.Relevant memories about the user:{memory_context}Use them only when relevant."
        },
        {"role": "user","content": user}]

    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    answer = response.choices[0].message.content

    print(f"\nBot: {answer}")

    print("\nSaving to memory...")

    memory.add(
        [
            {"role": "user", "content": user},
            {"role": "assistant", "content": answer}
        ],
        user_id=USER_ID
    )
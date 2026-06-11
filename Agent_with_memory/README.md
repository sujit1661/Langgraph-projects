# AI Chatbot with Mem0 Memory and Groq

A simple AI chatbot built using **Groq LLMs** and **Mem0 Cloud** to provide personalized conversations with long-term memory. The chatbot can remember user preferences, personal information, goals, skills, and other important details across conversations.

---

# Features

- Long-term memory using Mem0 Cloud
- Fast response generation with Groq
- Automatic memory extraction
- Semantic memory retrieval
- User-specific memories
- Persistent context across sessions
- Simple command-line interface
- Easy integration with AI agents and LangGraph

---

# Tech Stack

- Python
- Mem0 Cloud
- Groq API
- Python Dotenv

---

# Project Architecture

```text
User Query
     ↓
Mem0 Search
     ↓
Retrieve Relevant Memories
     ↓
Groq LLM
     ↓
Generate Response
     ↓
Mem0 Add
     ↓
Store Important Memories
```

---

# How Mem0 Works Internally

Mem0 is not a traditional database that stores every chat message.

Instead, it acts as a memory layer for AI applications.

When a conversation is added to Mem0, it analyzes the messages and extracts only important information that may be useful in future conversations.

---

## Memory Extraction Process

```text
Conversation
      ↓
LLM-Based Analysis
      ↓
Identify Important Information
      ↓
Create Memory Objects
      ↓
Generate Embeddings
      ↓
Store in Memory Store
```

### Example

Conversation:

```text
User: My name is Sujit.
User: I am a final year AI student.
User: I like Python.
User: Thanks.
```

Mem0 may extract:

```text
User's name is Sujit.
User is a final year AI student.
User likes Python.
```

Ignored:

```text
Thanks.
```

because it provides no long-term value.

---

# What Information Does Mem0 Store?

Mem0 usually stores:

### Personal Information

```text
My name is Sujit.
I am from Pune.
```

### Preferences

```text
I like Python.
My favorite color is blue.
```

### Goals

```text
I want to learn LangGraph.
I am preparing for interviews.
```

### Skills

```text
I know Python and AI development.
```

### Ongoing Projects

```text
I am building a CodeX coding platform.
```

### Relationships

```text
My friend Rahul is a software engineer.
```

---

# What Information Does Mem0 Ignore?

Examples:

```text
Hi
Hello
Okay
Thanks
Good Morning
How are you?
```

These messages generally have no future relevance and are not useful memories.

---

# How Memories Are Stored

Each memory is stored as a structured memory object.

Conceptually:

```json
{
  "memory": "User likes Python",
  "user_id": "sujit",
  "timestamp": "2026-06-11",
  "embedding": [0.21, -0.55, 0.78, ...]
}
```

Each memory contains:

| Field | Description |
|---------|-------------|
| memory | Human-readable memory |
| user_id | User associated with the memory |
| timestamp | Creation or update timestamp |
| embedding | Vector representation of memory |

---

# What Are Embeddings?

Embeddings are numerical representations of text.

Example:

```text
User likes Python
```

becomes:

```text
[0.21, -0.55, 0.78, 0.13, ...]
```

These vectors capture the semantic meaning of text.

This allows Mem0 to retrieve relevant memories even when the wording changes.

---

# Memory Retrieval Process

When a user asks a question:

```text
What programming language do I enjoy?
```

Mem0:

```text
User Query
      ↓
Generate Query Embedding
      ↓
Search Similar Memory Embeddings
      ↓
Find Relevant Memories
      ↓
Return Results
```

Example:

Stored Memory:

```text
User likes Python.
```

User Query:

```text
What programming language do I enjoy?
```

Even though the wording is different, vector similarity helps Mem0 retrieve the correct memory.

---

# Memory Update Process

Mem0 can update existing memories when new information conflicts with previous memories.

Example:

Stored Memory:

```text
Favorite language = Python
```

Later:

```text
My favorite language is Java.
```

Mem0 may replace the old memory with:

```text
Favorite language = Java
```

instead of storing contradictory information.

---

# Why Use Mem0?

Large Language Models have limited context windows.

Without memory:

```text
New Conversation
      ↓
LLM Forgets Previous Information
```

With Mem0:

```text
New Conversation
      ↓
Retrieve Relevant Memories
      ↓
Provide Personalized Response
```

This enables long-term personalization.

---

# Pros of Mem0

### Automatic Memory Extraction

No need to manually decide what should be stored.

### Personalized Responses

AI remembers user-specific information.

### Reduced Prompt Size

Only relevant memories are retrieved.

### Better User Experience

Creates more natural conversations.

### Semantic Search

Finds memories based on meaning rather than exact wording.

### Easy Integration

Works well with:

- LangGraph
- LangChain
- OpenAI
- Groq
- Gemini
- Claude

---

# Limitations of Mem0

### Not a Chat History Database

Mem0 stores memories, not complete conversations.

For complete chat history, use databases such as:

- PostgreSQL
- MongoDB
- MySQL

### Memory Extraction Is Not Perfect

Important details may occasionally be missed.

### Additional Cost

Cloud memory services may incur usage costs.

### Retrieval Is Not Guaranteed

Relevant memories may sometimes not be retrieved if similarity scores are low.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
MEM0_API_KEY=your_mem0_api_key
GROQ_API_KEY=your_groq_api_key
```

---

# Project Structure

```text
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

# Running the Application

```bash
python main.py
```

Example:

```text
Enter your query: Hi, my name is Sujit

Bot: Nice to meet you, Sujit.

Enter your query: What is my name?

Bot: Your name is Sujit.
```

Exit:

```text
Enter your query: exit
```

---

# Core Memory Operations

## Add Memory

```python
memory.add(
    [
        {"role": "user", "content": user},
        {"role": "assistant", "content": answer}
    ],
    user_id=USER_ID
)
```

---

## Search Memory

```python
memory.search(
    query=user,
    user_id=USER_ID
)
```

---

# Future Improvements

- LangGraph Integration
- Multi-Agent Support
- Streamlit UI
- Memory Visualization Dashboard
- Authentication System
- Chat History Database
- Web Deployment

---

# Author

**Sujit Sadalage**

B.Tech Artificial Intelligence and Data Science

Interests:

- Python Development
- Artificial Intelligence
- Generative AI
- Agentic AI
- LangGraph
- Web Development

---

# License

This project is created for educational and learning purposes.
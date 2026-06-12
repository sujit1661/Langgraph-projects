# AI Chatbot with Qdrant Memory and Groq

A conversational AI chatbot built using **Groq**, **Qdrant Cloud**, and **Mem0** for long-term memory management. The chatbot can remember important user information across conversations and retrieve relevant memories using semantic search.

---

# Features

- Conversational AI powered by Groq
- Long-term memory storage using Qdrant Cloud
- Semantic memory retrieval
- User-specific memory isolation
- Automatic memory extraction using Mem0
- Persistent memory across sessions
- Cloud-hosted vector database

---

# Tech Stack

- Python
- Groq
- Mem0
- Qdrant Cloud
- Sentence Transformers
- Python Dotenv

---

# Architecture

```text
User Message
      ↓
Search Memory
      ↓
Qdrant Vector Database
      ↓
Retrieve Relevant Memories
      ↓
Build Context
      ↓
Groq LLM
      ↓
Generate Response
      ↓
Store New Memory
      ↓
Qdrant Cloud
```

---

# How It Works

## Memory Storage

When a user sends a message:

```text
User: My name is Sujit.
```

Mem0 analyzes the conversation and extracts useful information.

Example memory:

```text
User's name is Sujit.
```

The memory is then converted into a vector embedding and stored inside Qdrant.

---

## Memory Retrieval

Later, if the user asks:

```text
What is my name?
```

The chatbot:

1. Converts the query into an embedding.
2. Searches Qdrant for similar memories.
3. Retrieves the most relevant memory.
4. Adds it to the prompt sent to Groq.

Result:

```text
Bot: Your name is Sujit.
```

---

# Internal Memory Flow

```text
Conversation
      ↓
Memory Extraction
      ↓
Generate Embeddings
      ↓
Store in Qdrant
      ↓
Vector Search
      ↓
Retrieve Relevant Memories
      ↓
Pass Context to Groq
```

---

# What Is Stored?

Example memory object:

```json
{
  "memory": "User likes Python",
  "user_id": "user_123"
}
```

Along with:

```text
Vector Embedding
Metadata
Timestamp
Memory ID
```

---

# Why Qdrant?

Qdrant is a vector database designed for semantic search.

Benefits:

- Fast similarity search
- Cloud hosting
- Metadata filtering
- Scalable memory storage
- Ideal for AI applications

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
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key

QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key

OPENAI_API_KEY=your_openai_key
```

---

# Project Structure

```text
chatbot_memory_qdrant/
│
├── main.py
├── .env
├── README.md
```

---

# Running the Application

```bash
python main.py
```

Example:

```text
Enter your query: Hi my name is Sujit

Bot: Nice to meet you Sujit.

Enter your query: What is my name?

Bot: Your name is Sujit.
```

Exit:

```text
Enter your query: exit
```

---

# Known Issues

## Vector Dimension Mismatch

If you switch embedding models after creating the collection, Qdrant may throw:

```text
Vector dimension error:
expected dim: 1536, got 384
```

Cause:

```text
Collection created using OpenAI embeddings (1536 dimensions)
Current embedding model uses 384 dimensions
```

Solution:

```text
Delete and recreate the collection
or
Use an embedding model matching the collection dimension
```

---

# Future Improvements

- Streamlit Web UI
- LangGraph Integration
- Multi-User Authentication
- Memory Visualization Dashboard
- Memory Categories
- Hybrid Search
- Agentic Workflows

---

# Learning Outcomes

This project demonstrates:

- Vector Databases
- Semantic Search
- AI Memory Systems
- Retrieval-Augmented Context
- Embeddings
- Long-Term Memory for Chatbots
- Cloud Vector Storage

---

# Author

**Sujit Sadalage**

B.Tech Artificial Intelligence and Data Science

Skills:

- Python
- Artificial Intelligence
- Generative AI
- Agentic AI
- LangGraph
- Vector Databases

---

# License

This project is intended for educational and learning purposes.
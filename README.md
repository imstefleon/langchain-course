# 🧠 LangChain Projects Portfolio

Welcome to my AI lab 🚀
This repository showcases a collection of projects focused on building intelligent systems using **LangChain**, LLMs, and real-world integrations.

---

## 🌟 About This Repository

This project explores how to design and build AI-powered systems that:

* Leverage **Large Language Models (LLMs)** (OpenAI & local models)
* Integrate **external tools and APIs**
* Implement **agent-based reasoning (ReAct)**
* Use **structured outputs with Pydantic**
* Solve real-world, multi-step problems

---

## 🛠️ Tech Stack

* 🧠 LangChain (Agents, Tools, LCEL)
* 🤖 OpenAI API
* 🦙 Ollama (local LLMs: Qwen, Gemma, Phi)
* 🌐 Tavily (real-time web search)
* 📦 Python
* ⚙️ dotenv (environment variable management)

---

## 📂 Projects Included

### 🔎 AI Agent with Tool Calling

An intelligent agent capable of selecting and using tools dynamically.

**Features:**

* ReAct reasoning loop
* Dynamic tool selection
* Integration with Tavily Search

---

### 🛒 Shopping Assistant Agent

A rule-based agent simulating a smart shopping assistant.

**Features:**

* Strict tool usage constraints
* Multi-step reasoning (price → discount)
* Controlled decision flow via prompt engineering

---

### 🌐 Web Search Agent

An agent connected to real-time web data.

**Tools:**

* Tavily Search API

---

### 🧪 Local LLM Agent (Ollama)

Run agents locally without relying on external APIs.

**Models used:**

* Qwen
* Gemma
* Phi

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-projects.git
cd langchain-projects
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

## 🚀 Running the Projects

```bash
python main.py
```

or:

```bash
python agent.py
```

---

## 🧠 Concepts Explored

* ReAct Agents
* Tool Calling
* Prompt Engineering
* Structured Outputs (Pydantic)
* Multi-step reasoning
* Local vs Cloud LLMs
* Agent loops

---

## 📈 Future Improvements

* [ ] Migration to LangGraph
* [ ] Persistent memory
* [ ] RAG (Retrieval-Augmented Generation)
* [ ] Agent evaluation & benchmarking
* [ ] API deployment (FastAPI / Streamlit)

---

## 💡 About Me

AI Engineer specialized in building intelligent systems using LLMs, autonomous agents, and real-world integrations.

---

## 🦁 Philosophy

Building technology that doesn’t just work…
but leaves a lasting impact.

---

## ⭐ If you like this project

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Contributing improvements
- 📢 Sharing with others

---

<div align="center">

**Built with ❤️ by Stef Leon**

</div>


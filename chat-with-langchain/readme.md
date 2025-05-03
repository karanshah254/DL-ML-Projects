# 🧠 PDF Q&A with Groq + LangChain

This project enables you to **interact with a PDF document** using [LangChain](https://www.langchain.com/), [Groq](https://console.groq.com/) LLMs, and local [Hugging Face](https://huggingface.co/) embeddings. You can load a PDF, ask questions about its content, and get instant AI-powered answers in the terminal or VS Code Jupyter Notebook.

---

## 🚀 Features
- 📄 Load and process PDF files
- ✂️ Chunk and embed text using `sentence-transformers`
- 📚 Store and retrieve relevant content with FAISS vector search
- 🤖 Generate answers using Groq-hosted LLMs (e.g., `llama3-8b-8192`)
- 💬 Ask questions in an interactive terminal or notebook environment
- 💻 Streamlit App support for cool UI.

---

## 📦 Installation
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup
1. Create a .env file in root and add Groq API Key
```GROQ_API_KEY=your_actual_groq_api_key```
2. Pass your own file
```loader = PyPDFLoader("path/to/your/document.pdf")```
3. Run the notebook or script. You'll be able to ask questions like:
```bash
Ask a question (or type 'exit' to quit): What is the document about?
Answer: This document discusses the...
```

---

## Supported Groq Models
1. **llama3-8b-8192**
2. **gemma-7b-it**
- >Refer this for model updates [Groq Models](https://console.groq.com/docs/deprecations)

---

## 📚 Tech Stack
1. Langchain
2. Groq API
3. Hugging Face Transformers
4. FAISS for vector search
5. Python script file or jupyter notebook (VS Code compatible)
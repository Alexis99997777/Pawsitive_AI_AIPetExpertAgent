# 🐾 Pawsitive AI — AI Pet Expert Agent (LangChain + RAG)

Pawsitive AI is a full-stack AI-powered web application that helps pet owners make safer and more informed decisions about pet care, nutrition, and products.

The system is built using **LangChain**, **Retrieval-Augmented Generation (RAG)**, and **OpenAI GPT models**, with carefully designed system prompts and guardrails to ensure safety, accuracy, and responsible product recommendations.

<h4>frontend website:https://pawsitiveai.netlify.app/</h4>
<h4>backend website:https://pawsitive-ai-aipetexpertagent.onrender.com</h4>
<h4>backend API Test docs(based on Swagger):https://pawsitive-ai-aipetexpertagent.onrender.com/docs</h4>


## ✨ Key Features

### 🧠 AI Pet Expert Agent
- Custom **SYSTEM_PROMPT** defining persona, safety rules, and output constraints
- Friendly, professional tone designed specifically for pet owners
- Enforced response structure with follow-up questions

### 🧩 LangChain-Based Agent Logic
- Uses LangChain to structure LLM interactions
- Separates:
  - Prompt design
  - Retrieval logic
  - Model invocation
- Designed for extensibility (tools, memory, chains)

### 📚 Retrieval-Augmented Generation (RAG)
- Integrates a lightweight RAG pipeline for pet-related knowledge
- Retrieves relevant context from a curated local knowledge base before calling the LLM
- Reduces hallucinations and improves factual accuracy

### 🛡 Safety-First Design
- Explicit disclaimer for medical-related questions (“not a veterinarian”)
- Guardrails to prevent unsafe or misleading advice
- Controlled temperature and prompt constraints

### 🛍 Product Recommendation Rules
- Recommends **1–3 real products only**
- At least one product must be available on **Chewy.com**
- Uses **Chewy search links only**:

## 🧱 Tech Stack

### Frontend
- HTML / CSS / JavaScript
- Tailwind CSS (CDN)
- Deployed on **Netlify**

### Backend
- Python
- FastAPI
- LangChain
- OpenAI official Python SDK
- Deployed on **Render**

### AI & Data
- OpenAI GPT-4o
- LangChain chains and prompt templates
- Local knowledge base for RAG

---

👩‍💻 Author

<b>Built by Alexis</b>
<p>Graduate CS student with a focus on backend engineering, distributed systems, and AI-powered applications.</p>


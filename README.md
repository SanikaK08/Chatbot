# 🧑‍💼 AI-Powered HR Chatbot with Admin Panel

This project is a Flask + Node.js based AI-powered HR Chatbot that helps employees with HR-related queries by fetching answers from company policy documents. It includes an **interactive chat interface** for employees and an **admin panel** for HR managers to manage documents and update the chatbot knowledge base.

"This project was built using open-source tools like Flask, LangChain, Pinecone, and Google Gemini API."
---

## 📌 Features

### ✅ Employee Chatbot Interface

* Chat UI similar to standard chat apps (floating bot icon, expandable/minimizable chat window)
* Blue-themed design with user and bot icons
* Instant AI responses to HR queries
* Gemini HuggingFace-based RAG pipeline backend

### ✅ Admin Panel

* Upload new company policy documents (PDFs)
* View the list of existing uploaded documents
* Trigger vector embedding and indexing process (to update chatbot's knowledge base)

### ✅ Backend (Python Flask)

* Gemini 1.5 Flash (Google Generative AI) based answer generation
* LangChain RAG (Retrieval-Augmented Generation) pipeline
* Pinecone vector database for semantic search over uploaded documents
* Document parsing, text chunking, and embedding handling

### ✅ Frontend (HTML/CSS/JS)

* Static HTML and CSS for UI

---

## 🛠️ Tech Stack

| Layer      | Technology                                      |
| ---------- | ----------------------------------------------- |
| Backend AI | Flask, LangChain, Gemini AI, Pinecone           |
| Frontend   | HTML, CSS, JavaScript                           |
| Storage    | Pinecone Vector DB, Local File System for PDFs  |
| Embeddings | HuggingFace Sentence Transformers               |

---

## 📂 Project Structure

```
AI-chatbot/

|── app.py
├── helper.py
├── prompt.py
├── data/                # Uploaded PDFs
│   └── ...                  
├── templates/
│   ├── index.html        # Chatbot UI
│   ├── admin.html        # Admin panel
├── static / 
│   ├── style.css
│   ├── chatbot.png
|   ├── hr.png
|   ├── user.png
│   
└── requirements.txt
```

---

## ✅ Setup Instructions

### API Keys Required


| Service       | How to get the API key                                                                                      |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| Google Gemini | From Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey) |
| Pinecone      | From Pinecone dashboard: [https://app.pinecone.io/](https://app.pinecone.io/)                               |


Steps:

1. Create a .env file in your backend folder.

2. Add the following:

PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_gemini_api_key



### Backend (Flask):

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Run backend:

```bash
python app.py
```

---


## ✅ Usage

### Chatbot (Employee View):

* Visit: `http://localhost:5000`
* Click the chatbot icon in the bottom-right corner
* Ask your HR questions

### Admin Panel (HR Admin View):

* Visit: `http://localhost:5000/admin.html`
* Upload new documents
* View existing documents
* Trigger vector database updates


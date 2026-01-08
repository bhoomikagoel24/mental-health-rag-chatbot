# 🧠 Mental Health AI Chatbot  

### Medical Assistant Chatbot using RAG (Retrieval-Augmented Generation)

A domain-specific **Medical / Mental Health AI Chatbot** built using **Retrieval-Augmented Generation (RAG)** to provide context-aware, reliable responses from medical reference data.  
The system combines semantic search with large language models to improve answer accuracy and relevance.

---

## 🚀 Project Overview

This chatbot assists users by answering medical and mental-health-related queries using trusted reference material instead of relying only on a language model’s general knowledge.

It uses:
- **Vector-based semantic retrieval**
- **Prompt-engineered LLM responses**
- **Basic safety disclaimers for medical guidance**

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Frameworks & Libraries:**
  - LangChain
  - FastAPI
  - Gemini API
- **Embedding & Retrieval:**
  - Vector embeddings
  - Semantic search (RAG pipeline)
- **Frontend:** HTML (Jinja templates)
- **Environment:** Python Virtual Environment (venv)

---

## 🧪 How It Works (RAG Pipeline)
1. Medical reference content is converted into embeddings
2. Embeddings are stored in a vector database
3. User queries are semantically matched with relevant documents
4. Retrieved context is injected into a custom prompt
5. Gemini API generates a grounded, context-aware response


## 🧩 Features

- 📚 Retrieval-Augmented Generation (RAG) pipeline
- 🔍 Context-aware medical question answering
- 🧠 Embedding-based semantic document search
- ✍️ Custom prompt engineering for medical domain
- ⚠️ Safety disclaimers for medical responses
- 🌐 API-based chatbot interface

---

## 📂 Project Structure
```bash
ROOT_DIRECTORY/
├── datasets/                 # Medical & mental health datasets
├── resource/                 # Jupyter notebooks for experiments
├── src/
│   ├── helper.py             # Utility functions
│   ├── prompt.py             # Prompt templates
│   └── __init__.py
├── templates/
│   └── chat.html             # Frontend UI
├── app.py                    # FastAPI application
├── store_index.py            # Vector store creation
├── requirements.txt          # Project dependencies
├── setup.py                  # Package setup
├── helper.txt                # Setup instructions (ignored in git)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://...............................
cd Medjcsnjk
```

---
###  2. Set up virtual environment
```bash
python -m venv venv
```

* Activate on Linux / Mac
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a file named .env in the root of the project and add your API keys:
```bash
PINECONE_API_KEY=your_pinecone_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
```

Note: Adjust variable names based on your code.

### 5. Build the vector index
```bash
python store_index.py
```

### 6. Run the application
```bash
python app.py
```

---

## 📚 Datasets Used

1. **Reddit Depression Dataset**
   - Text-based dataset consisting of user-generated posts related to depression.
   - Helps capture real-world mental health expressions and informal language patterns.

2. **Depression Survey Dataset**
   - Structured survey-based dataset containing responses related to depression and mental health indicators.
   - Provides factual and questionnaire-based context for reliable retrieval.

Both datasets were preprocessed, cleaned, and converted into embeddings before being used in the RAG pipeline.

---

## 📊 Dataset Quality Evaluation

```text
Combined Dataset Quality Score: 79.49 / 100
Overall Rating: ⭐⭐⭐ Good
```

## 👩‍💻 Author
Bhoomika Goel
Aspiring AI-Driven Software Engineer
`Learning purpose
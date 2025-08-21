# 📚 LearnGPT – AI Tutor with Modules

> A personalized **AI-powered tutor** that delivers lessons, quizzes, and progress tracking across topics like Machine Learning, SQL, and System Design. Built with **RAG, LangChain, and Streamlit**.

---

## 🚀 Overview

**LearnGPT** is designed to transform the way students learn technical concepts.  
Instead of static notes or pre-made videos, it provides an **interactive, adaptive learning platform** where learners can:

- 📖 Study structured lessons (Markdown modules)  
- 🧠 Take AI-generated quizzes for active recall  
- ✅ Track progress with checkpoints  
- 🔍 Ask contextual questions with **RAG-powered Q&A**  
- 🎯 Learn at their own pace with personalized feedback  

This project is especially useful for students, professionals upskilling, and AI-driven education research.

## ✨ Features

- 📚 **Modular Lessons** – Interactive lessons in Markdown format (ML, SQL, more coming soon)  
- 🧠 **AI-Generated Quizzes** – JSON-based quizzes dynamically integrated into lessons  
- ✅ **Checkpoints** – Track your progress and reinforce learning  
- 🔍 **RAG-Powered Q&A** – Ask contextual questions about the content and get precise answers  
- 💾 **Save Progress** – Resume exactly where you left off  
- 🎨 **Streamlit UI** – Clean, user-friendly interface for seamless learning  

---

## 🛠 Tech Stack

| Layer            | Tools / Libraries |
|------------------|-------------------|
| UI               | Streamlit |
| AI Orchestration | LangChain |
| Vector DB        | ChromaDB |
| LLMs             | OpenAI / Ollama / SentenceTransformers |
| Data             | Markdown lessons, JSON quizzes |
| Utilities        | Python, Checker module |

## 📂 Repository Structure

```
LearnGPT/
├── app/
│   ├── main.py              # Streamlit entry point
│   ├── components.py        # UI components
├── llm/
│   └── tutor_agent.py       # Core AI tutor agent
├── modules/                 # Learning modules (Markdown)
│   ├── ml.md
│   └── sql.md
├── quizzes/                 # Quiz data (JSON format)
│   ├── ml.json
│   └── sql.json
├── utils/
│   └── checker.py           # Quiz validation logic
├── requirements.txt          # Dependencies
├── run_streamlit.bat         # Quick start script (Windows)
├── LearnGPT_PRD.txt          # Product design document
└── README.md
```

---

## ⚡ Installation & Local Deployment

### 🔧 Prerequisites
- Python 3.10+  
- OpenAI or Ollama API key  
- Git  

### 📥 Clone the Repository
```bash
git clone https://github.com/saxil/LearnGPT.git
cd LearnGPT
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔐 Configure Environment Variables
Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
```

### ▶️ Run the Application
```bash
streamlit run app/main.py
```

Or on Windows, simply double-click:
```
run_streamlit.bat
```
## 🧠 Workflow

1. User selects a module (e.g., Machine Learning, SQL).  
2. Lesson content is loaded from Markdown files.  
3. **Tutor Agent** explains concepts and answers contextual questions.  
4. **Quizzes** are generated from JSON files to test understanding.  
5. **Checker Utility** validates quiz answers.  
6. Progress is saved for the next session.  

---

## 🔮 Roadmap

- 📘 Add more modules (System Design, NLP, Databases).  
- 🎤 Voice-enabled tutoring.  
- 🧩 Adaptive difficulty quizzes.  
- 📊 Analytics dashboard for progress tracking.  
- 🌐 Multi-user support with login.  
- ⚡ Offline AI agent support with Ollama.  

---

## 🤝 Contributing

Contributions are welcome!  

To contribute:  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io) – for the interactive UI  
- [LangChain](https://www.langchain.com) – for LLM orchestration  
- [OpenAI](https://openai.com) & [Ollama](https://ollama.com) – for powering LLMs  
- [ChromaDB](https://www.trychroma.com) – for vector database management  
- [Markdown](https://daringfireball.net/projects/markdown/) – for module lessons  
- [JSON](https://www.json.org/) – for quiz datasets  

---

## ✨ Final Note

Built with 💡 passion, 📚 curiosity, and 🚀 a vision to make learning smarter.  
If you find this project helpful, please ⭐ star the repo and share it with friends and learners!  

Let’s redefine education with AI 🌟

# 📝 AI-Powered Resume Writer

An intelligent, full-stack web application that helps users generate professional resumes and cover letters using GPT-4. The app features a simple HTML/CSS/JS frontend, a Flask-based backend, OpenAI integration for content generation, and PDF export functionality.

---

## 🚀 Features

- ✨ AI-powered resume and cover letter generation using GPT-4
- 🖊️ Easy-to-use form-based UI with live preview
- ✅ Input validation and resume formatting

---

## 📁 Project Structure



resume-writer/
├── client/ # Plain HTML/CSS/JavaScript frontend
│ ├── index.html # Input form for user data
│ ├── preview.html # Generated resume preview
│ ├── styles/ # CSS styling
│ └── js/ # Frontend logic and API handlers
├── server/ # Flask backend
│ ├── api/ # API endpoints for resume generation
│ ├── services/ # GPT, PDF, and validation logic
│ ├── models/ # ORM model for resume storage
│ ├── templates/ # Jinja2 template rendering
│ ├── utils/ # Config and environment management
│ ├── app.py # Main application entry point
├── pdf_engine/ # Resume HTML template for PDF rendering
├── database/ # DB schema and seeders
├── docker/ # Docker & Docker Compose setup
├── tests/ # Unit and integration tests
├── .env # Environment variables (API keys, DB path)
└── README.md # Project documentation




---

## 🧠 Technologies Used

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Flask (Python)
- **AI Integration:** Gemini 1.5 flash (via `openai_service.py`)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-writer.git
cd resume-writer

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
├── client/                     # Plain HTML/CSS/JavaScript frontend
│   ├── index.html              # Homepage with input form
│   ├── preview.html            # Resume/cover letter preview page
│   ├── styles/
│   │   └── main.css            # All frontend styling
│   └── js/
│       └── main.js             # Form logic and API integration
│
├── server/                     # Flask backend
│   ├── api/
│   │   └── routes.py           # API endpoints for GPT, PDF, DB
│   ├── services/
│   │   ├── openai_service.py   # GPT-4 generation logic
│   │   ├── pdf_service.py      # PDF conversion logic
│   │   └── validation_service.py
│   ├── models/
│   │   └── resume_model.py     # ORM model for resumes
│   ├── templates/
│   │   └── resume_template.html # Jinja2 template for rendering resumes
│   ├── utils/
│   │   └── config.py           # Config and environment loader
│   ├── app.py                  # Main Flask app entry
│   └── __init__.py             # App factory init
│
├── pdf_engine/                 # PDF rendering module
│   └── resume_template.html    # HTML template used for PDF export
│
├── database/                   # DB schema and seeders
│   ├── models.py
│   └── seed.py
│
├── docker/                     # Containerization setup
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
│
├── tests/                      # Unit and integration tests
│   ├── api_tests.py
│   └── unit/
│       ├── test_openai_service.py
│       └── test_pdf_service.py
│
├── .env                        # Environment variables
└── README.md                   # Project instructions and documentation




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

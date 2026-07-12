# 🤖 AI Personalized Networking Assistant

An AI-powered professional networking platform designed to help users create meaningful connections, improve communication, and gain insights from networking events.

The application uses Artificial Intelligence to analyze events, generate personalized conversation starters, verify information, maintain activity history, and provide smart networking assistance.

---

# ✨ Features

## 🏠 AI Networking Dashboard
- Professional AI-powered dashboard interface.
- Personalized welcome experience.
- Quick access to all networking modules.
- Modern responsive UI.

---

## 🧠 Event Analyzer

Analyze professional events such as:

- Conferences
- Workshops
- Seminars
- Networking sessions

### Capabilities:
- Extract important event themes.
- Identify networking opportunities.
- Generate AI-based event insights.

---

## 💬 Conversation Generator

Generate personalized professional conversation starters.

### Features:
- Enter person's name.
- Enter organization/company details.
- Provide event or discussion topics.
- Generate AI-based networking questions and introductions.

---

## 📚 Fact Checker

Verify information before professional discussions.

### Features:
- Analyze statements/topics.
- Provide information verification.
- Reduce misinformation during networking conversations.

---

## 🤖 AI Networking Assistant

Provides AI guidance for:

- Professional introductions.
- Networking strategies.
- Follow-up messages.
- Communication improvement.
- Career networking suggestions.

---

## 👤 User Profile Management

Users can:

- View personal details.
- Update profile information.
- Manage networking interests.
- Store preferences.

Profile information includes:

- Name
- Email
- Role
- Phone number
- Networking interests

---

## 🕘 Activity History

Tracks user activities:

- Event analysis history
- Generated conversations
- Fact verification records

Stored securely using Firebase Realtime Database.

---

## ⭐ Feedback System

Users can submit feedback to improve the platform.

Stores:

- User name
- Feedback message
- Email
- Timestamp

---

# 🛠️ Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- Responsive Dashboard UI

## Backend

- Python
- FastAPI
- Uvicorn

## Artificial Intelligence

- Groq API
- Gemini API

AI capabilities include:

- Text generation
- Event analysis
- Conversation generation
- Intelligent suggestions

## Database

- Firebase Authentication
- Firebase Realtime Database

Used for:

- User profiles
- Activity history
- Feedback storage

---

# 📂 Project Structure

```
AI-Personalized-Networking-Assistant/

│
├── frontend/
│   │
│   ├── index.html
│   ├── login.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   │
│   ├── main.py
│   ├── event_analyzer.py
│   ├── conversation_generator.py
│   ├── fact_checker.py
│   ├── requirements.txt
│   └── .env
│
├── README.md
└── .gitignore

```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

Navigate into project:

```bash
cd AI-Personalized-Networking-Assistant
```

---

# 🔹 Backend Setup

Go to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file inside backend folder:

```
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Never expose API keys in frontend code.

---

# ▶️ Run Backend

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🌐 Run Frontend

Open:

```
frontend/index.html
```

or use VS Code Live Server.

---

# 🔥 Firebase Configuration

Firebase Realtime Database stores:

```
users
 |
 ├── user_email
       |
       ├── profile
       ├── history
       └── activities


feedback
 |
 └── feedback_records
```

---

# 🚀 Deployment

## Frontend Deployment

Supported platforms:

- Vercel
- Firebase Hosting

## Backend Deployment

Supported platforms:

- Render
- Railway
- Cloud platforms

After deployment:

Update API endpoint URLs in JavaScript.

---

# 🔒 Security Practices

- API keys stored using environment variables.
- Firebase database rules configured for authorized users.
- Sensitive information is not stored in frontend files.
- Authentication-based user data separation.

---

# 🎯 Future Enhancements

- Voice-based AI networking assistant.
- LinkedIn profile analysis.
- AI-generated networking reports.
- Calendar-based event recommendations.
- Smart follow-up email generation.
- Real-time networking recommendations.
- AI chatbot integration.

---

# 🎥 Project Demo

Project Working Video:

https://www.loom.com/share/f54a515791464705986fbd5eb7603cbf

---

# 👩‍💻 Developed By

**AI Personalized Networking Assistant**

An intelligent solution for improving professional networking through Artificial Intelligence.
# 🤖 AI Q&A Bot

> An AI-powered question-answering bot built for an intern assignment. Ask anything and get intelligent responses!

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [What I Learned](#what-i-learned)
- [Challenges & Solutions](#challenges--solutions)
- [Future Improvements](#future-improvements)

## ✨ Features

- 💬 **Natural Conversation**: Chat naturally with AI
- 🧠 **Context Awareness**: Remembers previous messages in conversation
- 🎨 **Two Interfaces**: 
  - Command-line for quick interactions
  - Beautiful Streamlit web UI (Stretch Goal!)
- 🔄 **Clear History**: Start fresh conversations anytime
- 📊 **Message Counter**: Track your conversation stats
- 🚀 **Easy Deployment**: Ready for Streamlit Cloud

## 🎥 Demo

### Command Line Version
```
🤖 AI Q&A Bot - Command Line Edition
============================================================
✅ Connected to OpenAI!

👤 You: What is Python?
🤖 AI: Python is a high-level programming language...

👤 You: quit
👋 Thanks for chatting! Goodbye!
```

### Web Interface
*(Add screenshot here after running)*

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-qa-bot.git
cd ai-qa-bot
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
```

## 💻 Usage

### Option 1: Command Line
```bash
python qa_bot.py
```

**Commands:**
- Type any question and press Enter
- Type `clear` to start a new conversation
- Type `quit` or `exit` to end

### Option 2: Web Interface (Stretch Goal!)
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## 📁 Project Structure

```
ai-qa-bot/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore file
├── qa_bot.py                # Command-line version
├── app.py                   # Streamlit web interface
├── DEVELOPMENT_LOG.md       # My development journey
└── screenshots/             # App screenshots
```

## 📚 What I Learned

### Technical Skills
1. **API Integration**: Connected to OpenAI's API and handled responses
2. **Environment Variables**: Learned to secure API keys using `.env` files
3. **Error Handling**: Implemented try-catch blocks for robust error management
4. **UI Development**: Created both CLI and web interfaces
5. **State Management**: Used session state in Streamlit for conversation history

### Problem-Solving
- **Challenge**: API key not loading
  - **Solution**: Used `python-dotenv` and verified file location
  
- **Challenge**: Conversation context not maintained
  - **Solution**: Implemented message history array

- **Challenge**: Streamlit app not updating
  - **Solution**: Used `st.session_state` for persistent data

### Tools & Resources Used
- 🔍 **Google/ChatGPT**: For debugging errors and learning syntax
- 📖 **OpenAI Docs**: API documentation and best practices
- 📺 **YouTube**: Streamlit tutorials
- 📝 **StackOverflow**: Troubleshooting specific issues

## 🎯 Challenges & Solutions

### Challenge 1: Setting Up Python Environment
**Problem**: Confusion between `python` and `python3` commands

**What I tried:**
1. Typed `python --version` - didn't work
2. Googled "python command not found"
3. Found I needed to use `python3` on Mac/Linux

**Solution**: Used `python3` and created an alias

### Challenge 2: API Key Security
**Problem**: How to use API key without exposing it in code?

**What I tried:**
1. First hardcoded the key (bad practice!)
2. Researched "how to hide API keys python"
3. Learned about environment variables

**Solution**: Implemented `.env` file with `python-dotenv`

### Challenge 3: Managing Conversation Context
**Problem**: Bot forgot previous messages

**What I tried:**
1. Read OpenAI docs about conversation history
2. Implemented message array
3. Tested with follow-up questions

**Solution**: Pass entire conversation history to API

## 🚀 Deployment (Stretch Goal!)

### Deploy on Streamlit Cloud

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy on Streamlit**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Click "New app"
- Select your repository
- Add your `OPENAI_API_KEY` in Secrets
- Deploy!

### Alternative: Render.com
See `DEPLOYMENT.md` for Render deployment instructions.

## 🔮 Future Improvements

- [ ] Add voice input/output
- [ ] Support multiple AI models (GPT-4, Claude, etc.)
- [ ] Save conversation history to database
- [ ] Add user authentication
- [ ] Export conversations as PDF
- [ ] Add typing indicator animation
- [ ] Support image-based questions
- [ ] Multi-language support

## 🤝 Contributing

This is a learning project, but suggestions are welcome!

## 📄 License

MIT License - feel free to use this for learning!

## 👨‍💻 Author

Built with ❤️ and lots of Googling for the Intern Assignment

**Time Spent**: ~4 hours (including learning, debugging, and documentation)

**Key Takeaway**: Building is the best way to learn. Every error taught me something new!

---

### 💡 Tips for Future Interns

1. **Don't fear errors** - They're learning opportunities
2. **Document everything** - Future you will thank present you
3. **Start small** - Get basic version working first
4. **Google is your friend** - Everyone does it, even senior developers
5. **Add polish gradually** - Basic working > Perfect but incomplete

**Questions?** Open an issue or reach out!

---

*Built as part of the Intern Assignment Challenge*
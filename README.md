# 🐍 My Python Journey

A record of my progress learning Python from zero to building real projects.

---

## 📅 Timeline

| Period | What I Did |
|--------|------------|
| [2026] | Started learning Python |
| [2026] | Completed FreeCodeCamp course |
| [2026] | Started Jarvis chatbot assistant |
| [2026] | Built Personal Task CLI Manager |

---

## 🎓 Courses & Certificates

### FreeCodeCamp
- **Course:** [Scientific Computing with Python / Data Analysis with Python / etc.]
- **Certificate:** "In progress"
- **What I learned:** Variables, functions, loops, file handling, JSON, argparse, etc.

### Other Tutorials
- YouTube - Mosh Python
- YouTube - Corey Schafer

---

## 🛠️ Projects

### 1. Jarvis - Chatbot Assistant
**Status:** 🚧 Ongoing

A voice-activated personal assistant inspired by Iron Man's Jarvis.  
The goal is to build a chatbot that can listen to voice commands, speak responses, and perform tasks.

**Current progress:**
- ✅ Set up project structure
- ✅ Created glue script (main entry point)
- 🚧 Implementing core features

**Planned features:**
- Voice recognition (speech to text)
- Text-to-speech responses
- Tell time and date
- Open applications and websites
- Search the web
- Tell jokes
- Weather updates
- Basic conversation

**What I'm learning:**
- Speech recognition (`speech_recognition`)
- Text-to-speech (`pyttsx3`)
- Working with APIs
- Modular code structure
- Error handling for real-world input

**Tech stack (planned):**
- `speech_recognition` - voice input
- `pyttsx3` - voice output
- `webbrowser` - open websites
- `datetime` - time and date
- External APIs - weather, news, Wikipedia

---

### 2. Personal Task CLI Manager
**Status:** ✅ Complete

A command-line task manager that lets you:
- Add, delete, update tasks
- Mark tasks as complete
- Search tasks by keyword
- Tasks persist in a JSON file

**What I learned:**
- Working with JSON files (read/write)
- `argparse` for command-line interfaces
- List comprehensions
- Dictionaries and lists
- File paths with `pathlib`
- Function design (single responsibility)

**How to run:**
```bash
python3 tasks.py add "Buy groceries"
python3 tasks.py list
python3 tasks.py complete 1
python3 tasks.py search "groceries"
python3 tasks.py delete 1
python3 tasks.py list-all
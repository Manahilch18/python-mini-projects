# ✅ Smart To-Do Manager

A feature-rich **command-line task manager** built with pure Python. Add, view, complete, delete, and search tasks — with priority levels, persistent file storage, and live statistics.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- ➕ **Add tasks** with a name and priority level (High / Medium / Low)
- 📋 **View all tasks** with status and priority in a numbered list
- ✔️ **Mark tasks as done** by selecting from the list
- 🗑️ **Delete tasks** by number with confirmation
- 🔍 **Search tasks** by keyword (case-insensitive)
- 📊 **Statistics dashboard** — total, completed, and pending task counts
- 💾 **Auto-save & auto-load** — data persists across sessions via `tasks.txt`
- ⚡ **Zero dependencies** — uses only built-in Python

---

## 🗂️ Menu Options

```
=========================
 SMART TO-DO MANAGER
=========================
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Search Task
6. Show Statistics
7. Exit
```

| Option | Description |
|---|---|
| 1 | Add a new task with name and priority |
| 2 | View the full task list with status and priority |
| 3 | Mark a task as Completed by its number |
| 4 | Permanently delete a task by its number |
| 5 | Search tasks by a keyword in the task name |
| 6 | Show total, completed, and pending task counts |
| 7 | Exit the program |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the App

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/smart-todo-manager.git
cd smart-todo-manager

# 2. Run the script
python todo_manager.py
```

---

## 📁 Project Structure

```
smart-todo-manager/
├── todo_manager.py   # Main application script
├── tasks.txt         # Auto-generated task storage file
└── README.md         # This file
```

---

## 💡 Example Usage

```
Enter your choice: 1
Enter task name: Build portfolio website
Enter priority (High/Medium/Low): High
Task added successfully!

Enter your choice: 2

===== TASK LIST =====
1. Build portfolio website | Status: Pending | Priority: High

Enter your choice: 3
1. Build portfolio website | Status: Pending | Priority: High

Enter task number to complete: 1
Task marked as completed!

Enter your choice: 6

===== TASK STATISTICS =====
Total Tasks     : 1
Completed Tasks : 1
Pending Tasks   : 0
```

---

## 💾 Data File Format

Tasks are saved to `tasks.txt` automatically after every change:

```
Build portfolio website|Completed|High
Write blog post|Pending|Medium
Fix login bug|Pending|Low
```

Each line follows the format: `name|status|priority`

> The file is loaded automatically on startup so your tasks are always available.

---

## 🔮 Future Improvements

- [ ] Add due dates and deadline reminders
- [ ] Sort tasks by priority or status
- [ ] Filter view by priority (show only High priority tasks)
- [ ] Store data in JSON or SQLite for better scalability
- [ ] Colored terminal output using the `colorama` library
- [ ] GUI version using Tkinter or a web app with Streamlit

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
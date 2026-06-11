# 🔐 Password Analyzer

A simple **command-line password strength checker** built with pure Python. Instantly analyzes your password and rates it as Weak, Medium, or Strong based on key security criteria.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🔎 **Checks 5 security criteria** in real time
- 📊 **Strength rating** — Weak, Medium, or Strong
- 🧾 **Detailed breakdown** of each criterion passed or failed
- ⚡ **Zero dependencies** — uses only built-in Python string methods
- 🖥️ **Instant results** — no loops, no waiting

---

## 📋 How Scoring Works

Each criterion adds **1 point** to the score (max 5):

| Criterion | Requirement |
|---|---|
| ✅ Length | At least 8 characters |
| ✅ Uppercase | Contains at least one uppercase letter (A–Z) |
| ✅ Lowercase | Contains at least one lowercase letter (a–z) |
| ✅ Digit | Contains at least one number (0–9) |
| ✅ Special Character | Contains at least one symbol (e.g. `@`, `#`, `!`) |

**Strength Ratings:**

| Score | Strength |
|---|---|
| 5 | 🟢 Strong |
| 3 – 4 | 🟡 Medium |
| 0 – 2 | 🔴 Weak |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the Script

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/password-analyzer.git
cd password-analyzer

# 2. Run the script
python password_analyzer.py
```

---

## 📁 Project Structure

```
password-analyzer/
├── password_analyzer.py   # Main script
└── README.md              # This file
```

---

## 💡 Example Output

```
Enter your password: Hello@123

Password Analyzer
--------------------
Password      : Hello@123
Length >= 8   : True
Has Uppercase : True
Has Lowercase : True
Has Digit     : True
Has Special   : True

Password Strength: Strong 🟢
```

```
Enter your password: hello

Password Analyzer
--------------------
Password      : hello
Length >= 8   : False
Has Uppercase : False
Has Lowercase : True
Has Digit     : False
Has Special   : False

Password Strength: Weak 🔴
```

---

## 🔮 Future Improvements

- [ ] Mask password input using the `getpass` module for security
- [ ] Suggest improvements when the password is Weak or Medium
- [ ] Check against a list of common passwords (e.g. `123456`, `password`)
- [ ] Add a password generator for strong random passwords
- [ ] Build a GUI version using Tkinter or Streamlit

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
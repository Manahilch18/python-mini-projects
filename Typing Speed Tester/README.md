# ⌨️ Typing Speed Tester

A simple **command-line typing speed test** built with pure Python. Measures your typing speed in Words Per Minute (WPM), counts mistakes, and calculates accuracy — all in seconds.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🎲 **Random sentence** selected from a built-in pool each round
- ⏱️ **Accurate timer** using Python's `time` module
- 📈 **WPM calculation** — words per minute based on actual time taken
- ❌ **Mistake counter** — character-by-character comparison including length differences
- 🎯 **Accuracy percentage** — how closely your input matched the original sentence
- ⚡ **Zero dependencies** — uses only built-in Python modules

---

## 📊 How Metrics Are Calculated

| Metric | Formula |
|---|---|
| **Time Taken** | `end_time − start_time` (in seconds) |
| **WPM** | `(words typed ÷ time taken) × 60` |
| **Mistakes** | Character mismatches + length difference |
| **Accuracy** | `((total chars − mistakes) ÷ total chars) × 100` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the Script

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/typing-speed-tester.git
cd typing-speed-tester

# 2. Run the script
python typing_tester.py
```

---

## 📁 Project Structure

```
typing-speed-tester/
├── typing_tester.py   # Main script
└── README.md          # This file
```

---

## 💡 Example Output

```
===== Typing Speed Tester =====

Type the following sentence:

Artificial intelligence is changing the world.

Press Enter when ready...

Start typing:
Artificial intelligence is changing the world.

===== RESULTS =====
Time Taken             : 6.43 seconds
Words Per Minute (WPM) : 65.32
Mistakes               : 0
Accuracy               : 100.00%
```

---

## 📝 Built-in Sentence Pool

The tester randomly picks one of these sentences each round:

- *"Python is a powerful programming language."*
- *"Practice makes perfect in coding."*
- *"Artificial intelligence is changing the world."*
- *"Learning Python is fun and useful."*
- *"Consistency is the key to success."*

> You can easily add more sentences to the `sentences` list in the script.

---

## 🔮 Future Improvements

- [ ] Multiple difficulty levels (short, medium, long sentences)
- [ ] Expanding the sentence pool from a text file or API
- [ ] Best score tracking across sessions
- [ ] Highlight mistakes character by character
- [ ] Replay option without restarting the script
- [ ] GUI version using Tkinter or a web app with Streamlit

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
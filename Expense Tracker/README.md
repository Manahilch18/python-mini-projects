# 💸 Expense Tracker

A simple and interactive **command-line expense tracker** built with pure Python — no external libraries required.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- ➕ **Add expenses** with a name, amount, and category
- 📋 **View all expenses** in a clean list
- 🏷️ **Update categories** for existing expenses
- 💰 **Calculate total** spending instantly
- 🔁 **Interactive menu loop** — runs until you choose to exit

---

## 🖥️ Menu Options

```
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Expenses by Category
4. Show Total
5. Exit
```

| Option | Description |
|---|---|
| 1 | Add a new expense (name, amount, category) |
| 2 | View all recorded expenses |
| 3 | Update/assign categories to existing expenses |
| 4 | Show the total of all expenses |
| 5 | Exit the program |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the App

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/expense-tracker.git
cd expense-tracker

# 2. Run the script
python expense_tracker.py
```

---

## 📁 Project Structure

```
expense-tracker/
├── expense_tracker.py   # Main application script
└── README.md            # This file
```

---

## 💡 Example Usage

```
===== Expense Tracker =====
Choose an option: 1
Enter expense name: Coffee
Enter amount: 3.50
Enter category: Food
Expense added successfully!

Choose an option: 2
Coffee: $3.5: Food:

Choose an option: 4
Total expenses: $3.5
```

---

## 🔮 Future Improvements

- [ ] Save and load expenses from a file (CSV or JSON)
- [ ] Filter expenses by category
- [ ] Set a monthly budget and track overspending
- [ ] Add date/time to each expense
- [ ] Build a GUI version with Tkinter or Streamlit

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

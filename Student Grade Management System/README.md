# 🎓 Student Grade Management System

A fully-featured **command-line student grade manager** built with pure Python. Add students, record subject marks, auto-calculate averages and grades, and save/load data to a file — all from a simple interactive menu.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 👤 **Add students** with duplicate detection
- 📝 **Record marks** for any number of subjects per student
- 📊 **Auto-calculate** average and letter grade per student
- 📋 **View individual** student reports or **all students at once**
- 💾 **Save & load** data to/from a `students.txt` file
- 🛡️ **Input validation** — handles missing students and empty marks gracefully
- ⚡ **Zero dependencies** — uses only built-in Python

---

## 🗂️ Menu Options

```
===== Student Grade Management System =====
1. Add Student
2. Add Marks
3. View Student Report
4. View All Students
5. Save Data
6. Load Data
7. Exit
```

| Option | Description |
|---|---|
| 1 | Add a new student by name |
| 2 | Enter marks for multiple subjects for a student |
| 3 | View a single student's marks, average, and grade |
| 4 | View all students with their full reports |
| 5 | Save all data to `students.txt` |
| 6 | Load previously saved data from `students.txt` |
| 7 | Exit the program |

---

## 🏅 Grading Scale

| Average Score | Grade |
|---|---|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| Below 50 | F |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the App

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/student-grade-management.git
cd student-grade-management

# 2. Run the script
python grade_manager.py
```

---

## 📁 Project Structure

```
student-grade-management/
├── grade_manager.py   # Main application script
├── students.txt       # Auto-generated data file (after saving)
└── README.md          # This file
```

---

## 💡 Example Usage

```
===== Student Grade Management System =====
Enter your choice: 1
Enter student name: Alice
Student added successfully!

Enter your choice: 2
Enter student name: Alice
How many subjects? 3
Enter marks for Subject 1: 88
Enter marks for Subject 2: 92
Enter marks for Subject 3: 76
Marks added successfully!

Enter your choice: 3
Enter student name: Alice

----- Student Report -----
Name   : Alice
Marks  : [88.0, 92.0, 76.0]
Average: 85.33
Grade  : A
```

---

## 💾 Data File Format

Data is saved to `students.txt` in a simple plain-text format:

```
Alice:88.0,92.0,76.0
Bob:70.0,65.0,80.0
Charlie:
```

Each line follows the pattern `name:mark1,mark2,...` — students with no marks are saved with an empty marks field.

---

## 🔮 Future Improvements

- [ ] Store data in JSON or CSV for better portability
- [ ] Search and delete students
- [ ] Per-subject labels (e.g. Math, Science, English)
- [ ] Class-wide statistics (highest average, top student)
- [ ] Export reports to PDF
- [ ] GUI version using Tkinter or a web app with Streamlit

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
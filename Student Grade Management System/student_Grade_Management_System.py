students = {} 
# Function to Add Student 
def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!")
    else:
        students[name] = []
        print("Student added successfully!") 
# Function to Add Marks 
def add_marks():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found!")
        return
    num_subjects = int(input("How many subjects? "))
    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)
    students[name] = marks
    print("Marks added successfully!") 
# Calculate Grade 
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"
# View One Student Report 
def view_student():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found!")
        return
    marks = students[name]
    if len(marks) == 0:
        print("No marks available.")
        return
    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    print("\n----- Student Report -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade) 
# View All Students 
def view_all_students():
    if not students:
        print("No students found.")
        return
    print("\n===== All Students =====")
    for name, marks in students.items():
        if len(marks) == 0:
            print(f"\nName: {name}")
            print("Marks: Not Added")
            continue
        average = sum(marks) / len(marks)
        grade = calculate_grade(average)
        print(f"\nName: {name}")
        print("Marks:", marks)
        print("Average:", round(average, 2))
        print("Grade:", grade)
# Save Data to File 
def save_data():
    with open("students.txt", "w") as file:
        for name, marks in students.items():
            marks_str = ",".join(map(str, marks))
            file.write(f"{name}:{marks_str}\n")
    print("Data saved successfully!") 
# Load Data from File 
def load_data():
    try:        
        with open("students.txt", "r") as file:
            students.clear()
            for line in file:
                line = line.strip()
                if ":" in line:
                    name, marks_data = line.split(":")
                    if marks_data:
                        marks = list(map(float, marks_data.split(",")))
                    else:
                        marks = []
                    students[name] = marks
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved file found.")
# Main Menu
while True:
    print("\n===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Student Report")
    print("4. View All Students")
    print("5. Save Data")
    print("6. Load Data")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        add_marks()
    elif choice == "3":
        view_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        save_data()
    elif choice == "6":
        load_data()
    elif choice == "7":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Try again.")
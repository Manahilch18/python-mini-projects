import json
import csv
import os

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)
    print(f"Expenses saved to {filename}")

def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_expenses_csv(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}")
def filter_by_category(expenses):
    if not expenses:
        print("No expenses found.")
        return
    category = input("Enter category to filter: ").lower()
    filtered = [e for e in expenses if e['category'].lower() == category]
    if not filtered:
        print(f"No expenses found in '{category}' category.")
    else:
        print(f"\n--- {category.upper()} Expenses ---")
        for e in filtered:
            print(f"{e['name']}: ${e['amount']}")
        total = sum(e['amount'] for e in filtered)
        print(f"Category Total: ${total}")
expenses = []
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Expenses by Category")
    print("4. Show Total")
    print("6. Save Expenses")
    print("7. Load Expenses")
    print("8. Filter by Category")
    print("9. Exit\n")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(f"{expense['name']}: ${expense['amount']}: {expense['category']}:")
    elif choice == "3":
        if not expenses:
            print("No expenses found.")
        else:
            for expense in expenses:
                category = input(f"Enter category for {expense['name']}: ")
                expense['category'] = category
            print("Categories added successfully!")
    elif choice == "4":
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total expenses: ${total}")
    elif choice == "6":
        save_expenses(expenses)
    elif choice == "7":
        expenses = load_expenses()
        print(f"{len(expenses)} expenses loaded!")
    elif choice == "8":
        filter_by_category(expenses)
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
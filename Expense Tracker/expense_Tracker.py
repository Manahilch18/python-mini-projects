expenses = []
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Expenses by Category")
    print("4. Show Total")
    print("5. Exit\n")
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
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
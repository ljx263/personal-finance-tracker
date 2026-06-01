# Personal Finance Tracker

expenses = []


def add_expense():

    print("\n--- Add Expense ---")

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully")


def show_expenses():

    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses recorded")

    else:
        for item in expenses:
            print(
                item["category"],
                "- $" + str(item["amount"])
            )


def total_spending():

    total = 0

    for item in expenses:
        total = total + item["amount"]

    print("\nTotal Spending: $" + str(total))


def category_summary():

    print("\n--- Spending By Category ---")

    categories = {}

    for item in expenses:

        category = item["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] = (
            categories[category]
            + item["amount"]
        )

    for category in categories:
        print(
            category,
            "- $" + str(categories[category])
        )


def highest_expense():

    print("\n--- Highest Expense ---")

    if len(expenses) == 0:
        print("No expenses recorded")
        return

    highest = expenses[0]

    for item in expenses:

        if item["amount"] > highest["amount"]:
            highest = item

    print(
        highest["category"],
        "- $" + str(highest["amount"])
    )


while True:

    print("\n--- PERSONAL FINANCE TRACKER ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total Spending")
    print("4. Spending By Category")
    print("5. Highest Expense")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        print("Program ended")
        break

    else:
        print("Invalid option")

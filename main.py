#ExpenseTracker

#Initialize an empty list to store expenses
expenses = []

#Initialize total_expenses variable
total_expenses = 0

#Function to add an expense
def add_expense(amount, description, category):
    expense = {"amount": amount, "description": description, "category": category}
    expenses.append(expense)
    print("Expense added successfully!!!!")

#Function to view monthly expense summary
def view_summary():
    total_expenses = 0  # Reset total_expenses to 0
    category_expenses = {}

    for expense in expenses:
        total_expenses += expense["amount"]
        category = expense["category"]
        if category in category_expenses:
            category_expenses[category] += expense["amount"]
        else:
            category_expenses[category] = expense["amount"]

    print("Monthly Expense Summary:")
    print(f"Total Expenses: {total_expenses}")
    print("Category-wise Expenses:")
    for category, amount in category_expenses.items():
        print(f"{category}: {amount}")

#Main program loop
while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        amount = float(input("Enter the amount spent:"))
        description = input("Enter a brief description:")
        category = input("Enter the category:")
        add_expense(amount, description, category)

    elif choice == "2":
        view_summary()

    elif choice == "3":
        print("Thank you for using Expense Tracker!!!!")
        break

    else:
        print("Invalid choice. Please try again.")
           
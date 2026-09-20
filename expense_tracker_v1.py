# Expense Tracker - Version 1
# Uses only simple Python: lists, loops, if-else and file handling.

FILE_NAME = "expenses.txt"

# Each expense is a small list: [date, category, amount]
expenses = []


def load_data():
    try:
        f = open(FILE_NAME, "r")
    except FileNotFoundError:
        return

    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            date = parts[0]
            category = parts[1]
            amount = float(parts[2])
            expenses.append([date, category, amount])
    f.close()


def save_data():
    f = open(FILE_NAME, "w")
    for item in expenses:
        f.write(item[0] + "," + item[1] + "," + str(item[2]) + "\n")
    f.close()


def add_expense():
    try:
        amount = float(input("Enter expense: "))
    except ValueError:
        print("That is not a valid number. Expense not added.")
        return

    if amount <= 0:
        print("Amount must be greater than zero. Expense not added.")
        return

    category = input("Category: ")
    if category == "":
        print("Category cannot be empty. Expense not added.")
        return

    date = input("Date (DD-MM-YYYY): ")
    if date == "":
        print("Date cannot be empty. Expense not added.")
        return

    expenses.append([date, category, amount])
    save_data()
    print("Expense added successfully.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print()
    print("----------- EXPENSES -----------")
    print()
    print("Date          Category      Amount")

    total = 0
    for item in expenses:
        print(item[0] + "    " + item[1] + "        Rs." + str(item[2]))
        total = total + item[2]

    print()
    print("Total: Rs." + str(total))


def total_expenses():
    total = 0
    for item in expenses:
        total = total + item[2]
    print("Total expenses: Rs." + str(total))


def search_expense():
    word = input("Enter category or date to search: ")
    found = 0

    for item in expenses:
        if item[0] == word or item[1] == word:
            print(item[0] + "    " + item[1] + "        Rs." + str(item[2]))
            found = found + 1

    if found == 0:
        print("No matching expense found.")


def delete_expense():
    if len(expenses) == 0:
        print("Nothing to delete.")
        return

    print()
    number = 1
    for item in expenses:
        print(str(number) + ". " + item[0] + "  " + item[1] + "  Rs." + str(item[2]))
        number = number + 1

    try:
        choice = int(input("Enter number to delete: "))
    except ValueError:
        print("That is not a valid number. Nothing deleted.")
        return

    if choice >= 1 and choice <= len(expenses):
        removed = expenses.pop(choice - 1)
        save_data()
        print("Deleted: " + removed[1] + " Rs." + str(removed[2]))
    else:
        print("Invalid number.")


# ---------------- main program ----------------

load_data()

while True:
    print()
    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Exit")
    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid choice. Please enter 1 to 6.")
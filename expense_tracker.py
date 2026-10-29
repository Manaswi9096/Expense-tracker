
import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

    return expenses


def add_expense():
    name = input("Enter expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in Rs: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category: ").strip()
    if not category:
        category = "Other"

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        fields = ["name", "amount", "category"]
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "amount": f"{amount:.2f}",
            "category": category
        })

    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- YOUR EXPENSES ---")
    total = 0

    for number, expense in enumerate(expenses, start=1):
        amount = float(expense["amount"])
        total += amount

        print(
            f"{number}. {expense['name']} | "
            f"Rs {amount:.2f} | {expense['category']}"
        )

    print(f"\nTotal spending: Rs {total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

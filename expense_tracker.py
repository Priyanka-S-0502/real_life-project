import os

FILE_NAME = "data.txt"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, 'w').close()

# 🔐 Login System
USERNAME = "admin"
PASSWORD = "1234"

def login():
    print("---- Login ----")
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid login!\n")
        return False


def add_income():
    amount = float(input("Enter income amount: "))
    with open(FILE_NAME, "a") as f:
        f.write(f"Income,{amount}\n")
    print("Income added successfully!")


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Bills/etc): ")
    with open(FILE_NAME, "a") as f:
        f.write(f"Expense,{amount},{category}\n")
    print("Expense added successfully!")


def view_transactions():
    with open(FILE_NAME, "r") as f:
        data = f.readlines()
        if not data:
            print("No transactions found!")
        else:
            for line in data:
                print(line.strip())


def calculate_balance():
    income = 0
    expense = 0

    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Income":
                income += float(parts[1])
            elif parts[0] == "Expense":
                expense += float(parts[1])

    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Balance: {income - expense}")


def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Expense":
                category = parts[2]
                amount = float(parts[1])
                summary[category] = summary.get(category, 0) + amount

    print("Expense Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")


def main():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Category Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            calculate_balance()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


# 🔑 Run only after login
if __name__ == "__main__":
    if login():
        main()
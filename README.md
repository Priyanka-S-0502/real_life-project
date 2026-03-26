
#  Smart Expense Tracker 

##  Project Description

This is a simple **Smart Expense Tracker** written in Python.
It helps users manage their daily income and expenses efficiently.

Users can add income, record expenses with categories, view transactions, and calculate balance.

---

##  Files in the Project

* **expense_tracker.py** – Main Python program
* **data.txt** – Stores transaction records

---

##  Features

* Add income 
* Add expenses with category
* View all transactions
* Calculate balance
* Category-wise expense summary
* Login system 
* File handling for data storage

---

##  Requirements

* Python 3

---

##  How to Run

```bash
python expense_tracker.py
```

---

##  Login Details

```
Username: admin
Password: 1234
```

---

#  Source Code

```python
import os

FILE_NAME = "data.txt"

if not os.path.exists(FILE_NAME):
    open(FILE_NAME, 'w').close()

USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    return user == USERNAME and pwd == PASSWORD

def add_income():
    amount = float(input("Enter income amount: "))
    with open(FILE_NAME, "a") as f:
        f.write(f"Income,{amount}\n")

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    with open(FILE_NAME, "a") as f:
        f.write(f"Expense,{amount},{category}\n")

def view_transactions():
    with open(FILE_NAME, "r") as f:
        for line in f:
            print(line.strip())

def calculate_balance():
    income = expense = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Income":
                income += float(parts[1])
            else:
                expense += float(parts[1])
    print("Balance:", income - expense)

def category_summary():
    summary = {}
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Expense":
                summary[parts[2]] = summary.get(parts[2], 0) + float(parts[1])
    print(summary)

def main():
    while True:
        print("\n1.Add Income\n2.Add Expense\n3.View\n4.Balance\n5.Summary\n6.Exit")
        ch = input("Enter choice: ")
        if ch == "1": add_income()
        elif ch == "2": add_expense()
        elif ch == "3": view_transactions()
        elif ch == "4": calculate_balance()
        elif ch == "5": category_summary()
        elif ch == "6": break

if login():
    main()
```

---

#  Output


<img width="764" height="672" alt="image" src="https://github.com/user-attachments/assets/432b1e0e-1d9a-454d-aeb6-2f219981aad6" />
<img width="774" height="729" alt="image" src="https://github.com/user-attachments/assets/404e8c8b-4c4d-4ce0-bfad-42c0215285ae" />
<img width="747" height="564" alt="image" src="https://github.com/user-attachments/assets/debdb6aa-0b56-406b-a264-21244342114c" />



---

#  Result

The **Smart Expense Tracker** application was successfully implemented using Python.

The program allows users to:

* Manage income and expenses
* Store data using file handling
* Calculate balance accurately
* View categorized expense summary

 The system works efficiently and is useful for **real-time financial tracking**.

---
#  Author

Priyanka S 212224040255

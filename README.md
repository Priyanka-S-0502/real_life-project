
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

```
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE_NAME = "data.txt"

if not os.path.exists(FILE_NAME):
    open(FILE_NAME, 'w').close()

USERNAME = "admin"
PASSWORD = "1234"

# ---------------- LOGIN ----------------
def login():
    user = simpledialog.askstring("Login", "Enter username:")
    pwd = simpledialog.askstring("Login", "Enter password:", show='*')

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Success", "Login successful!")
        return True
    else:
        messagebox.showerror("Error", "Invalid login!")
        return False

# ---------------- FUNCTIONS ----------------
def add_income():
    amount = simpledialog.askfloat("Income", "Enter income amount:")
    if amount:
        with open(FILE_NAME, "a") as f:
            f.write(f"Income,{amount}\n")
        messagebox.showinfo("Success", "Income added!")

def add_expense():
    amount = simpledialog.askfloat("Expense", "Enter expense amount:")
    category = simpledialog.askstring("Category", "Enter category:")

    if amount and category:
        with open(FILE_NAME, "a") as f:
            f.write(f"Expense,{amount},{category}\n")
        messagebox.showinfo("Success", "Expense added!")

def view_transactions():
    with open(FILE_NAME, "r") as f:
        data = f.read()
        if data:
            messagebox.showinfo("Transactions", data)
        else:
            messagebox.showinfo("Transactions", "No data found!")

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

    messagebox.showinfo(
        "Balance",
        f"Income: {income}\nExpense: {expense}\nBalance: {income - expense}"
    )

def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Expense":
                category = parts[2]
                amount = float(parts[1])
                summary[category] = summary.get(category, 0) + amount

    result = "\n".join([f"{k}: {v}" for k, v in summary.items()])
    messagebox.showinfo("Category Summary", result if result else "No data")

# ---------------- MAIN APP ----------------
def main_app():
    root = tk.Tk()
    root.title("Smart Expense Tracker")
    root.geometry("300x350")

    tk.Label(root, text="Expense Tracker", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Add Income", width=20, command=add_income).pack(pady=5)
    tk.Button(root, text="Add Expense", width=20, command=add_expense).pack(pady=5)
    tk.Button(root, text="View Transactions", width=20, command=view_transactions).pack(pady=5)
    tk.Button(root, text="View Balance", width=20, command=calculate_balance).pack(pady=5)
    tk.Button(root, text="Category Summary", width=20, command=category_summary).pack(pady=5)
    tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

    root.mainloop()

# ---------------- RUN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # hide main window

    if login():
        main_app()
```

---

#  Output

<img width="1914" height="1003" alt="image" src="https://github.com/user-attachments/assets/81caf998-3458-4cfc-98f7-1b5b8cc8cd8d" />

<img width="1905" height="991" alt="image" src="https://github.com/user-attachments/assets/f6d064ac-11a5-4f69-bb29-189b0187c7f7" />

<img width="269" height="224" alt="image" src="https://github.com/user-attachments/assets/286ad7ef-2ebe-495c-b5d9-bb4c34b2cb5a" />

<img width="1914" height="991" alt="image" src="https://github.com/user-attachments/assets/9ddb47db-182a-4807-9df1-5d1ded87d211" />

<img width="1907" height="998" alt="image" src="https://github.com/user-attachments/assets/d71b05dc-ac96-4665-8a11-4b5b0c84fc66" />

<img width="1915" height="1009" alt="image" src="https://github.com/user-attachments/assets/faca46eb-ee12-4e25-b48a-c347dafce0c1" />

<img width="1900" height="1003" alt="image" src="https://github.com/user-attachments/assets/6c231370-aa5c-4e37-817d-afd30374d1b7" />

<img width="1919" height="1006" alt="image" src="https://github.com/user-attachments/assets/84c018a4-27ee-40b2-9046-bbb5fed1b43b" />

<img width="1908" height="1006" alt="image" src="https://github.com/user-attachments/assets/60b9d438-da81-47c8-86a7-e4431b62fadb" />



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

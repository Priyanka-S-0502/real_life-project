import tkinter as tk
from tkinter import messagebox
import os

# ------------------ Bank Class ------------------

class Bank:
    def __init__(self, filename="bank_data.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass

    def create_account(self, acc_no, name, balance):
        if self.account_exists(acc_no):
            return False
        with open(self.filename, "a") as file:
            file.write(f"{acc_no},{name},{balance}\n")
        return True

    def account_exists(self, acc_no):
        with open(self.filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    return True
        return False

    def get_balance(self, acc_no):
        with open(self.filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    return float(data[2])
        return None

    def update_balance(self, acc_no, new_balance):
        lines = []
        with open(self.filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    lines.append(f"{acc_no},{data[1]},{new_balance}\n")
                else:
                    lines.append(line)
        with open(self.filename, "w") as file:
            file.writelines(lines)

    def deposit(self, acc_no, amount):
        balance = self.get_balance(acc_no)
        if balance is not None:
            balance += amount
            self.update_balance(acc_no, balance)
            return True
        return False

    def withdraw(self, acc_no, amount):
        balance = self.get_balance(acc_no)
        if balance is not None and balance >= amount:
            balance -= amount
            self.update_balance(acc_no, balance)
            return True
        return False


# ------------------ GUI Class ------------------

class BankApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Simple Banking System")
        self.root.geometry("400x400")

        tk.Label(root, text="Banking System", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text="Account No").pack()
        self.acc_entry = tk.Entry(root)
        self.acc_entry.pack()

        tk.Label(root, text="Name").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Amount").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Button(root, text="Create Account", command=self.create_account).pack(pady=5)
        tk.Button(root, text="Deposit", command=self.deposit).pack(pady=5)
        tk.Button(root, text="Withdraw", command=self.withdraw).pack(pady=5)
        tk.Button(root, text="Check Balance", command=self.check_balance).pack(pady=5)

    def create_account(self):
        acc = self.acc_entry.get()
        name = self.name_entry.get()
        amount = self.amount_entry.get()

        if acc and name and amount:
            if self.bank.create_account(acc, name, float(amount)):
                messagebox.showinfo("Success", "Account Created Successfully")
            else:
                messagebox.showerror("Error", "Account Already Exists")
        else:
            messagebox.showwarning("Warning", "All Fields Required")

    def deposit(self):
        acc = self.acc_entry.get()
        amount = self.amount_entry.get()

        if self.bank.deposit(acc, float(amount)):
            messagebox.showinfo("Success", "Amount Deposited")
        else:
            messagebox.showerror("Error", "Account Not Found")

    def withdraw(self):
        acc = self.acc_entry.get()
        amount = self.amount_entry.get()

        if self.bank.withdraw(acc, float(amount)):
            messagebox.showinfo("Success", "Amount Withdrawn")
        else:
            messagebox.showerror("Error", "Insufficient Balance or Account Not Found")

    def check_balance(self):
        acc = self.acc_entry.get()
        balance = self.bank.get_balance(acc)
        if balance is not None:
            messagebox.showinfo("Balance", f"Current Balance: {balance}")
        else:
            messagebox.showerror("Error", "Account Not Found")


# ------------------ Run App ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
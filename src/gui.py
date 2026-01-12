import tkinter as tk
from tkinter import messagebox
from datetime import date

from src.db import create_table
from src.add_expense import add_expense
from src.reports import monthly_report, get_total_expense

# ---------------- CONFIG ----------------
MONTHLY_BUDGET = 3000  # change if needed

# Ensure DB & table exist
create_table()

# ---------------- FUNCTIONS ----------------
def add_expense_gui():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get().strip()

        if not category:
            messagebox.showerror("Error", "Category is required")
            return

        today = date.today().isoformat()
        add_expense(amount, category, today)

        total = get_total_expense()

        if total > MONTHLY_BUDGET:
            messagebox.showwarning(
                "Budget Alert ⚠️",
                f"Monthly budget exceeded!\n\nBudget: ₹{MONTHLY_BUDGET}\nSpent: ₹{total}"
            )
        else:
            messagebox.showinfo("Success", "Expense added successfully!")

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")


def show_report():
    monthly_report()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("300x260")
root.resizable(False, False)

tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(
    root,
    text="Add Expense",
    command=add_expense_gui,
    bg="#4CAF50",
    fg="white",
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="View Report",
    command=show_report,
    width=20
).pack()

root.mainloop()

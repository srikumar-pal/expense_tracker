from src.db import create_table
from src.add_expense import add_expense
from src.reports import monthly_report
from datetime import date


create_table()

while True:
    print("\n1. Add Expense\n2. View Report\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        amt = float(input("Amount: "))
        cat = input("Category: ")
        today = date.today().isoformat()
        add_expense(amt, cat, today)
        print("Expense added!")

    elif choice == "2":
        monthly_report()

    elif choice == "3":
        break

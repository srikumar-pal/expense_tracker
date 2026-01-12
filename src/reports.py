import sqlite3
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt


# -------- BASE PATH (EXE + NORMAL SUPPORT) --------
def get_base_path():
    # PyInstaller EXE support
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = get_base_path()

DATA_DIR = os.path.join(BASE_DIR, "data")
CHART_DIR = os.path.join(BASE_DIR, "charts")

DB_PATH = os.path.join(DATA_DIR, "expenses.db")
CHART_PATH = os.path.join(CHART_DIR, "monthly_report.png")


# -------- MONTHLY REPORT --------
def monthly_report():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(CHART_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No expenses found!")
        return

    summary = df.groupby("category")["amount"].sum()

    print("\nExpense Summary by Category:")
    print(summary)

    # -------- BAR CHART --------
    plt.figure(figsize=(6, 4))
    summary.plot(kind="bar")
    plt.title("Monthly Expense Report (Bar Chart)")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

    # -------- PIE CHART + SAVE --------
    plt.figure(figsize=(6, 6))
    summary.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Monthly Expense Distribution")
    plt.ylabel("")
    plt.tight_layout()

    plt.savefig(CHART_PATH)
    plt.show()

    print(f"\n📁 Chart saved at: {CHART_PATH}")


# -------- TOTAL EXPENSE (FOR BUDGET ALERT) --------
def get_total_expense():
    os.makedirs(DATA_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT amount FROM expenses", conn)
    conn.close()

    if df.empty:
        return 0

    return df["amount"].sum()

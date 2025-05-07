import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import csv

# Connect to SQLite database (or create it)
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

# Create the expenses table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        amount REAL NOT NULL
    )
''')
conn.commit()

# ----------------------- Functions -----------------------

def add_expense():
    """Add a new expense to the database."""
    date = input("Enter date (YYYY-MM-DD) [Leave empty for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (e.g., Food, Rent, Transport): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    cur.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
                (date, category, description, amount))
    conn.commit()
    print("✅ Expense added.\n")

def view_expenses():
    """Display all expenses in the database."""
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    if not rows:
        print("No expenses found.\n")
        return

    print("\n📄 All Expenses:\n")
    print("{:<5} {:<12} {:<15} {:<25} {:<10}".format("ID", "Date", "Category", "Description", "Amount"))
    print("-" * 70)
    for row in rows:
        print("{:<5} {:<12} {:<15} {:<25} {:<10.2f}".format(*row))
    print()

def show_summary():
    """Show total amount spent per category."""
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cur.fetchall()
    if not rows:
        print("No expenses to summarize.\n")
        return

    print("\n📊 Expense Summary by Category:\n")
    for row in rows:
        print(f"{row[0]:<15}: ₹{row[1]:.2f}")
    print()

def delete_expense():
    """Delete an expense entry by ID."""
    view_expenses()
    exp_id = input("Enter the ID of the expense to delete: ")
    cur.execute("DELETE FROM expenses WHERE id = ?", (exp_id,))
    conn.commit()
    print("🗑️ Expense deleted.\n")

def export_to_csv():
    """Export all expense records to a CSV file."""
    with open('expenses_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Date', 'Category', 'Description', 'Amount'])
        cur.execute("SELECT * FROM expenses")
        writer.writerows(cur.fetchall())
    print("📁 Data exported to 'expenses_export.csv'.\n")

def show_summary_chart():
    """Display a pie chart of expenses by category using matplotlib."""
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cur.fetchall()

    if not data:
        print("No data available for chart.\n")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("💸 Expense Distribution by Category")
    plt.axis('equal')  # Keeps the pie chart circular
    plt.show()

# ----------------------- Main Program -----------------------

def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Delete Expense")
        print("5. Export to CSV")
        print("6. Show Summary Chart")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            show_summary_chart()
        elif choice == '7':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

    conn.close()

if __name__ == "__main__":
    main()

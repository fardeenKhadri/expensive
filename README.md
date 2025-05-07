# 💰 Personal Expense Tracker (Python + SQLite + Matplotlib)

A simple and effective command-line application to track your daily expenses using Python, SQLite, and Matplotlib. Easily add, view, delete, and analyze your spending with a user-friendly interface and helpful visual charts.

---

## 📌 Features

- ✅ Add new expenses with date, category, description, and amount
- 📄 View all recorded expenses in a clean table
- 📊 Show total spending by category
- 🗑️ Delete expenses by ID
- 📁 Export all data to a CSV file
- 🎨 Visualize expenses with a pie chart (category-wise) using Matplotlib

---

## 📂 Project Structure

```

expnse.py               # Main Python script
expenses.db             # SQLite database (auto-created)
expenses\_export.csv    # Optional CSV export file
README.md               # Project documentation

````

---

## 🛠️ Installation

### 1. Clone the repository or download the Python file:

```bash
git clone https://github.com/The-Assassin-SK/expensive
cd expense-tracker
````

### 2. Install required libraries:

Only `matplotlib` is required externally (Python and SQLite are built-in).

```bash
pip install matplotlib
```

---

## ▶️ How to Use

Run the Python script:

```bash
python expnse.py
```

You’ll see a menu like this:

```
=== Personal Expense Tracker ===
1. Add Expense
2. View Expenses
3. Show Summary
4. Delete Expense
5. Export to CSV
6. Show Summary Chart
7. Exit
```

Select options by entering the corresponding number.

---

## 📊 Pie Chart Visualization

Use option **6: Show Summary Chart** to view a pie chart showing how your expenses are distributed across categories.

Example:

* 🍔 Food: 40%
* 🚕 Transport: 25%
* 🏠 Rent: 35%

---

## 💡 Future Improvements

* GUI version using Tkinter or PyQt
* Monthly and yearly filtering
* User authentication and multiple user support

---

## 📄 License

This project is open-source and free to use for educational and personal use.

---


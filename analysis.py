import json
import os

def analyze_expenses():
    """
    Reads expense_data.json and prints a summary report.
    """
    filename = 'expense_data.json'
    
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        print("Please export data from the web app first.")
        return
    
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
        
        if not expenses:
            print("No expenses found in the file.")
            return
        
        total_spent = sum(expense['amount'] for expense in expenses)
        transaction_count = len(expenses)
        
        print("=" * 40)
        print("EXPENSE ANALYSIS REPORT")
        print("=" * 40)
        print(f"Total Transactions: {transaction_count}")
        print(f"Total Amount Spent: ${total_spent:.2f}")
        print(f"Average per Transaction: ${total_spent / transaction_count:.2f}")
        print("=" * 40)
        
        print("\nDetailed Breakdown:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['name']}: ${expense['amount']:.2f} on {expense['date']}")
        
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_expenses()

#Expense Tracker and Planner
#Goal: Track all my expenses and eventually use it to manage my financial assets and do planning

# Ledger - list of all transactions
# Transaction - $, date, participants
# Expense - category
# Income - source
# Asset - value, depreciation, appreciation
# Stocks
# Capital goods
# Mutual Funds

import datetime
import csv
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Ledger:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def get_balance(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.amount
        return total
            
        
class Transaction:
    def __init__(self, amount, date, participants=[]):
        self.amount = amount
        self.date = date
        self.participants = participants

class Expense(Transaction):
    def __init__(self, amount, date, category, participants = []):
        super().__init__(-1*amount, date, participants)
        self.category = category
        
class Income(Transaction):
    def __init__(self, amount, date, participants, source):
        super().__init__(amount, date, participants)
        self.source = source
        


class ExpenseInsights: 
    def __init__(self): 
        self.expenses = []
        self.expensePerCategory = {}
    
    def add_expense(self, expense): 
        self.expenses.append(expense)
        
        expenseCategory = expense.category
        
        if (expenseCategory in self.expensePerCategory):
            self.expensePerCategory[expenseCategory] += (-1*expense.amount)
        else: 
            self.expensePerCategory[expenseCategory] = (-1*expense.amount)
        
    def totalExpenditure(self): 
        total = 0 
        for expense in expenses:
            total = total + 1
        return -1*total
    
    def totalExpensePerCategory(self): 
        return self.expensePerCategory
        

    def plot_expense_breakdown(insights):
        categories = list(insights.expensePerCategory.keys())
        totals = list(insights.expensePerCategory.values())

        # Check if there is data to plot
        if not totals:
           print("No data available to plot.")
           return

        plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    
        plt.title('Monthly Expense Breakdown')
        plt.axis('equal')  # Ensures the pie chart is a circle
    
        # Save and show
        plt.savefig('expense_breakdown.png')
        print("Visualization saved as 'expense_breakdown.png'")
        plt.show()



class DataExtractor: 
    def extract_expenses(dataSource):
        return dataSource.all_expenses()
        
        
class DataSource(ABC):
    @abstractmethod
    def all_expenses(self):
        pass

class CsvParser(DataSource): 
    def __init__(self, expense_csv_path):
        self.expense_path = expense_csv_path
    
    def all_expenses(self):
        expenses = []
        try:
            with open(self.expense_path, mode='r', encoding='utf-8') as file:
                # DictReader uses the first row as keys for each dictionary
                reader = csv.DictReader(file)
                for row in reader:
                    # Logic to convert the raw strings from CSV into Expense objects
                    try:
                        expense = Expense(
                            amount=float(row['amount']),
                            date=row['date'],
                            participants=row.get('participants', '').split(';'), # Assumes semicolon separated
                            category=row['category']
                        )
                        expenses.append(expense)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping malformed row: {row} - Error: {e}")
        except FileNotFoundError:
            print(f"Error: The file at {self.expense_path} was not found.")
            
        return expenses

def main():
    my_ledger = Ledger()
    insights = ExpenseInsights()
    print("--- Welcome to the MIMS Expense Tracker ---")

    path = "expenses.csv"
    parser = CsvParser(path)
    
    imported_expenses = DataExtractor.extract_expenses(parser)
    
    for exp in imported_expenses:
        my_ledger.add_transaction(exp)
        insights.add_expense(exp)

    print(f"Successfully imported {len(imported_expenses)} expenses.")
    insights.plot_expense_breakdown()

if __name__ == "__main__":
    main()
             






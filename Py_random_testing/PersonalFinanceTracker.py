import datetime

class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.date.today()

class Budget:
    def __init__(self, income, expenses=None):
        self.income = income
        self.expenses = expenses if expenses else []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def remaining_balance(self):
        return self.income - self.total_expenses()

class FinanceTracker:
    def __init__(self):
        self.budgets = {}
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def create_budget(self, income):
        self.budgets[datetime.date.today()] = Budget(income)

    def get_expenses(self):
        return [transaction for transaction in self.transactions if transaction.amount < 0]

    def get_incomes(self):
        return [transaction for transaction in self.transactions if transaction.amount > 0]

    def get_total_expenses(self):
        return sum(abs(transaction.amount) for transaction in self.get_expenses())

    def get_total_incomes(self):
        return sum(transaction.amount for transaction in self.get_incomes())

    def get_balance(self):
        return self.get_total_incomes() - self.get_total_expenses()

def main():
    tracker = FinanceTracker()
    while True:
        print("\n1. Add transaction")
        print("2. Create budget")
        print("3. Get expenses")
        print("4. Get incomes")
        print("5. Get total expenses")
        print("6. Get total incomes")
        print("7. Get balance")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter transaction amount: "))
            category = input("Enter transaction category: ")
            date = input("Enter transaction date (YYYY-MM-DD): ")
            year, month, day = map(int, date.split('-'))
            date = datetime.date(year, month, day)
            transaction = Transaction(amount, category, date)
            tracker.add_transaction(transaction)
        elif choice == "2":
            income = float(input("Enter budget income: "))
            tracker.create_budget(income)
        elif choice == "3":
            expenses = tracker.get_expenses()
            for expense in expenses:
                print(f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")
        elif choice == "4":
            incomes = tracker.get_incomes()
            for income in incomes:
                print(f"Amount: {income.amount}, Category: {income.category}, Date: {income.date}")
        elif choice == "5":
            total_expenses = tracker.get_total_expenses()
            print(f"Total expenses: {total_expenses}")
        elif choice == "6":
            total_incomes = tracker.get_total_incomes()
            print(f"Total incomes: {total_incomes}")
        elif choice == "7":
            balance = tracker.get_balance()
            print(f"Balance: {balance}")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

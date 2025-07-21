import datetime
import matplotlib.pyplot as plt

class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.date.today()

class FinanceTracker:
    def __init__(self):
        self.income = []
        self.expenses = []
        self.budget = {}

    def add_income(self, amount, date=None):
        self.income.append(Transaction(amount, 'income', date))

    def add_expense(self, amount, category, date=None):
        self.expenses.append(Transaction(amount, category, date))

    def set_budget(self, category, amount):
        self.budget[category] = amount

    def get_balance(self):
        total_income = sum(t.amount for t in self.income)
        total_expenses = sum(t.amount for t in self.expenses)
        return total_income - total_expenses

    def get_expenses_by_category(self):
        expenses_by_category = {}
        for t in self.expenses:
            if t.category in expenses_by_category:
                expenses_by_category[t.category] += t.amount
            else:
                expenses_by_category[t.category] = t.amount
        return expenses_by_category

    def check_overspending(self):
        for category, amount in self.get_expenses_by_category().items():
            if category in self.budget and amount > self.budget[category]:
                print(f'Overspending in {category}: {amount} (budget: {self.budget[category]})')

    def visualize_expenses(self):
        categories = self.get_expenses_by_category().keys()
        amounts = self.get_expenses_by_category().values()
        plt.bar(categories, amounts)
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expenses by Category')
        plt.show()

def main():
    tracker = FinanceTracker()
    while True:
        print('1. Add income')
        print('2. Add expense')
        print('3. Set budget')
        print('4. Get balance')
        print('5. Get expenses by category')
        print('6. Check overspending')
        print('7. Visualize expenses')
        print('8. Exit')
        choice = input('Choose an option: ')
        if choice == '1':
            amount = float(input('Enter income amount: '))
            date = input('Enter date (yyyy-mm-dd): ')
            tracker.add_income(amount, datetime.datetime.strptime(date, '%Y-%m-%d').date())
        elif choice == '2':
            amount = float(input('Enter expense amount: '))
            category = input('Enter expense category: ')
            date = input('Enter date (yyyy-mm-dd): ')
            tracker.add_expense(amount, category, datetime.datetime.strptime(date, '%Y-%m-%d').date())
        elif choice == '3':
            category = input('Enter budget category: ')
            amount = float(input('Enter budget amount: '))
            tracker.set_budget(category, amount)
        elif choice == '4':
            print(f'Balance: {tracker.get_balance()}')
        elif choice == '5':
            print(tracker.get_expenses_by_category())
        elif choice == '6':
            tracker.check_overspending()
        elif choice == '7':
            tracker.visualize_expenses()
        elif choice == '8':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()

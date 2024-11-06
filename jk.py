# Budget Planner Program

class BudgetPlanner:
    def __init__(self, income):
        self.income = income
        self.expenses = {}
    
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def display_expenses(self):
        print("\n--- Expenses Breakdown ---")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount:.2f}")
    
    def total_expenses(self):
        return sum(self.expenses.values())
    
    def remaining_balance(self):
        return self.income - self.total_expenses()

# Function to display the budget summary
def display_summary(budget):
    print("\n--- Budget Summary ---")
    print(f"Total Income: ${budget.income:.2f}")
    print(f"Total Expenses: ${budget.total_expenses():.2f}")
    print(f"Remaining Balance: ${budget.remaining_balance():.2f}")
    print("-------------------------")

def main():
    income = float(input("Enter your total monthly income: $"))
    budget = BudgetPlanner(income)
    
    while True:
        print("\n1. Add Expense")
        print("2. Display Expenses")
        print("3. Show Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter the expense category (e.g., rent, groceries): ")
            amount = float(input(f"Enter the amount for {category}: $"))
            budget.add_expense(category, amount)
            print(f"Added {category} expense of ${amount:.2f}")
        
        elif choice == '2':
            budget.display_expenses()
        
        elif choice == '3':
            display_summary(budget)
        
        elif choice == '4':
            print("Exiting Budget Planner. Have a great day!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

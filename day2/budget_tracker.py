def budget_tracker():
    """Simple budget tracker that calculates remaining balance after expenses."""
    
    print("=" * 50)
    print("SIMPLE BUDGET TRACKER")
    print("=" * 50)
    print()
    
    # Get total monthly budget
    while True:
        try:
            total_budget = float(input("Enter your total monthly budget (LKR): "))
            if total_budget < 0:
                print("Budget cannot be negative. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print()
    print("Enter your expenses (type 'done' when finished):")
    print("-" * 50)
    
    # Get expenses until user types 'done'
    expenses = []
    expense_count = 1
    while True:
        user_input = input(f"Expense {expense_count} (LKR) or 'done': ").strip()
        
        # Check if user wants to exit
        if user_input.lower() == 'done':
            if len(expenses) == 0:
                print("Please enter at least one expense.")
                continue
            break
        
        # Try to convert to float
        try:
            expense = float(user_input)
            if expense < 0:
                print("Expense cannot be negative. Please enter a valid amount.")
                continue
            expenses.append(expense)
            expense_count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    
    # Calculate total expenses
    total_expenses = sum(expenses)
    
    # Calculate remaining balance
    remaining_balance = total_budget - total_expenses
    
    # Display results
    print()
    print("=" * 50)
    print("BUDGET SUMMARY")
    print("=" * 50)
    print(f"Total Monthly Budget:  LKR {total_budget:,.2f}")
    print("-" * 50)
    print("Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"  Expense {i}:         LKR {expense:,.2f}")
    print("-" * 50)
    print(f"Total Expenses:        LKR {total_expenses:,.2f}")
    print("=" * 50)
    
    # Display remaining balance with color coding
    if remaining_balance >= 0:
        print(f"Remaining Balance:     LKR {remaining_balance:,.2f} ✓")
    else:
        print(f"Remaining Balance:     LKR {remaining_balance:,.2f} (OVERSPENT)")
    
    print("=" * 50)
    
    # Warn if low funds
    if remaining_balance < 500 and remaining_balance >= 0:
        print("\033[91m\033[1m⚠️  WARNING: LOW FUNDS ⚠️\033[0m")
        print("\033[93mYour remaining balance is less than LKR 500\033[0m")


if __name__ == "__main__":
    budget_tracker()
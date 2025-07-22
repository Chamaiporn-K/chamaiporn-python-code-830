"""
Personal Finance Calculator
Student: [Chamaiporn konglae]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings
"""
monthly_income = float(input("User's monthly income in THB: "))
rent_cost = float(input("Monthly rent/housing cost: "))
food_budget = int(input("Monthly food budget in THB: "))
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percentage to invest: "))

emergency_fund = emergency_fund_percent ÷ 100
investment = investment_percent ÷ 100

Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget
Total Expenses = fixed + variable_expenses
Remaining Income = monthly_income - total expenses
Emergency_Fund_Amount = monthly_income × (emergency_fund_percent ÷ 100)
Investment_Amount = monthly_income × (investment_percent ÷ 100)
Available_For_Savings = remaining_income - emergency_fund - investment
Expense_Ratio = (total_expenses ÷ income) × 100

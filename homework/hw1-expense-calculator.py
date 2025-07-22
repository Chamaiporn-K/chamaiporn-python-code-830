"""
Personal Finance Calculator
Student: [Chamaiporn konglae]
Date: [23/07/2568]
Purpose: Calculate monthly budget and savings
"""
monthly_income = float(input("User's monthly income in THB: "))
rent_cost = float(input("Monthly rent/housing cost: "))
food_budget = int(input("Monthly food budget in THB: "))
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percentage to invest: "))

# คำนวณค่าใช้จ่าย
total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
# รายได้คงเหลือ
remaining_income = monthly_income - total_expenses
# การออมและการลงทุน
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund_amount - investment_amount
# สัดส่วนค่าใช้จ่าย
expense_ratio = (total_expenses / monthly_income) * 100
print("\n")
print("=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income} THB")
print(f"Fixed Expenses: {total_fixed_expenses} THB")
print(f"Variable Expenses: {total_variable_expenses} THB")
print(f"Total Expenses: {total_expenses} THB")
print(f"Remaining: {remaining_income} THB")
print("\n")
print("=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%):{emergency_fund_amount} THB")
print(f"Investment ({investment_percent}%):{investment_amount} THB")
print(f"Available for Savings:{available_for_savings} THB")
print("\n")
print("=== ANALYSIS ===")
print(f"Expense Ratio:{expense_ratio:.2f} %")
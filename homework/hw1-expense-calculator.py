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

# คำนวณเปอร์เซ็นต์
emergency_fund_rate = emergency_fund_percent / 100
investment_rate = investment_percent / 100
# คำนวณค่าใช้จ่าย
total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
# รายได้คงเหลือ
remaining_income = monthly_income - total_expenses
# การออมและการลงทุน
emergency_fund_amount = monthly_income * emergency_fund_rate
investment_amount = monthly_income * investment_rate
available_for_savings = remaining_income - emergency_fund_amount - investment_amount
# สัดส่วนค่าใช้จ่าย
expense_ratio = (total_expenses / monthly_income) * 100

print("=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income} THB")
print(f"Fixed Expenses: {total_fixed_expenses} THB")


#prompt user for financial details
monthly_income = input ("Enter your monthly income: ")
monthly_expenses = input ("Enter your monthly expenses: ")
#convert user input into floats for calculation
monthly_income = float (monthly_income)
monthly_expenses = float (monthly_expenses)
#calculate monthly savings
monthly_savings = (monthly_income - monthly_expenses)
#calculate annual savings inclusive of interest
projected_savings = int (monthly_savings * 12 + (monthly_savings *12 * 0.05))
#print results
print (f"your montly savings is {monthly_savings}")
print (f"your annual savings is {projected_savings}")
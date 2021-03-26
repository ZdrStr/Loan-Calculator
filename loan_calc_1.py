loan = int(input("Enter the loan principal:\n"))
calculate = input("What do you want to calculate?\n type 'm' for number of monthly payments,\n type 'p' for the monthly payment:\n")
if calculate == "m":
  monthly = int(input("Enter the monthly payment:\n"))
  print((loan / monthly) + (loan / monthly > 0))
elif calculate == "p":
  monthly_1 = int(input("Enter the number of months:\n"))
  print(((loan / monthly_1) + (loan / monthly_1 > 0)))

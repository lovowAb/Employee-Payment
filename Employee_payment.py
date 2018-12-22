"""
  Abdullahi Yusuf
  lovowAb
  Employee payment int .py
"""
print("Welcome to Payment System\n")
ID = input("Enter Employee ID: ")
WorkedHrs = eval(input("Enter Number of hours worked: "))
PerHrRate = eval(input("Enter hourly rate: "))
Gross_Pay = WorkedHrs * PerHrRate
tax = Gross_Pay * 0.1
net_Pay = Gross_Pay - tax
print()
print("Payment of Employee ", ID, " is $", net_Pay)

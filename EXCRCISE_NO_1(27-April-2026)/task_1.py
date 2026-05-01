# Write a program that takes salary as input. Using conditional statements, calculate the final tax
# based on the following rules: (Marks 3)
# • If the salary is less than 30,000 → Tax rate is 5%
# • If the salary is between 30,000 and 70,000 → Tax rate is 15%
# • If the salary is greater than 70,000 → Tax rate is 25%

salary=int(input("enter your salary:"))

if(salary<30000):
    TaX_5=salary*5/100
    salary=salary-TaX_5
    print("5% tax apply to your salary of :",TaX_5)
    print("your salary after 5% tax is:",salary)
elif(salary>30000 and salary<70000):
    TaX_15=salary*15/100
    salary=salary-TaX_15
    print("15% tax apply to your salary of :",TaX_15)
    print("your salary after 15% tax is:",salary)
else:
    TaX_25=salary*25/100
    salary=salary-TaX_25
    print("15% tax apply to your salary of :",TaX_25)
    print("your salary after 25% tax is:",salary)

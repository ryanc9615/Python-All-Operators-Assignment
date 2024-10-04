#User Input 
employee_name = input("Please enter name: ")
employee_age = int(input("Please enter age: "))
hourly_wage = int(input("Please enter hourly wage: "))
hours_worked = int(input("Please enter hours worked: "))

# Calculations

gross_pay = hourly_wage * hours_worked
overtime_pay = (hours_worked - 40) * (hourly_wage * 1.5)

print(gross_pay)
print(overtime_pay)

if hours_worked > 40: 
    print(overtime_pay)

if employee_age >= 60: 
    print("Eligible for retirement benefits")
else:
    print('')

if hours_worked > 40 and hourly_wage > 20: 
    print("High earner with overtime")

if hours_worked > 40: 
    total_pay = gross_pay + overtime_pay
    print(total_pay)

if employee_name == "Ryan": 
    print("You have chosen the selected employee")

if "a" in employee_name:
    print("Yes")

print(employee_age >> 1)
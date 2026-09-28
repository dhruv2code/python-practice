Salary = float(input("Enter the salary: "))
Perdaysalary = Salary / 30
dayspresent = int(input("Enter the number of days present: "))

monthsalary = dayspresent * Perdaysalary





if monthsalary >= 50000:
    hra = monthsalary * 20/100
    da = monthsalary * 10/100

elif monthsalary >=30000:
    hra = monthsalary * 15/100
    da = monthsalary * 8/100

else:
    hra = monthsalary * 10/100
    da = monthsalary * 5/100

total_salary = monthsalary + hra + da
print("monthly salary:", monthsalary)
print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total_salary)
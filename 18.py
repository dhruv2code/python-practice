Salary = 60000

if Salary >= 50000:
    hra = Salary * 20/100
    da = Salary * 10/100

elif Salary >=30000:
    hra = Salary * 15/100
    da = Salary * 8/100

else:
    hra = Salary * 10/100
    da = Salary * 5/100

total_salary = Salary + hra + da
print("Total Salary:", total_salary)
print("HRA:", hra)
print("DA:", da)
print("Basic Salary:", Salary)
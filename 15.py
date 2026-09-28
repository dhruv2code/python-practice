Hindi = int(input("Enter your marks in Hindi: "))
English = int(input("Enter your marks in English: "))
Maths = int(input("Enter your marks in Maths: "))

Total = Hindi + English + Maths
Percentage = (Total / 300) * 100
print("Total Marks: ", Total)
print("Percentage: ", Percentage)

if Percentage >= 90:
    print("Grade: A")
elif Percentage >= 80:
    print("Grade: B")
elif Percentage >= 70:
    print("Grade: C")
elif Percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")
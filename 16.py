Hindi = 90
English = 85
Maths = 95
Science = 80
Computer = 75
Total = Hindi + English + Maths + Science + Computer
Percentage = (Total / 500) * 100
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
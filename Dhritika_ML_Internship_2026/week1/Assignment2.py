#Find sum of first 10 natural numbers.
a = 0
for i in range(1, 11):
    a += i
print("Sum =", a)

#Find factorial of a number.
a = int(input("Enter a number: "))
fa= 1
for i in range(1, a + 1):
    fa *= i
print("Factorial =", fa)

#Print Fibonacci Series.
n = 15
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Find largest among 3 numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number =", a)
elif b >= a and b >= c:
    print("Largest number =", b)
else:
    print("Largest number =", c)

#Create Student Result System
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
subjects = 5
total_marks = 0
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks
percentage = total_marks / subjects
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"
print("RESULT")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
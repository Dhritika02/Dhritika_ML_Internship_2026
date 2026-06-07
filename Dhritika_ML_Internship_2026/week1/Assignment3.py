#Create a function to print first 10 natural numbers.
def a():
    for i in range(1, 11):
        print(i)
a()

#Create a function to calculate sum of first N natural numbers.
def naturaln(n):
    return n * (n + 1) // 2
n = int(input("Enter N: "))
print("Sum =", naturaln(n))

#Create a function to reverse a number.
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
n = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(n))

#Create a function to count digits in a number.
def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n //= 10
    return count
n = int(input("Enter a number: "))
print("Number of digits =", count_digits(n))

#Create a function to check palindrome number.
def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return original == reverse
n = int(input("Enter a number: "))
if is_palindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#Create a function to generate Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter number of terms: "))
fibonacci(n)

#Calculator Using Functions that contains the following features;-User selects operation
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter choice (1-4): "))
c = int(input("Enter first number: "))
d = int(input("Enter second number: "))
if choice == 1:
    print("Result =", add(c, d))
elif choice == 2:
    print("Result =", subtract(c, d))
elif choice == 3:
    print("Result =", multiply(c, d))
elif choice == 4:
    print("Result =", divide(c, d))
else:
    print("Invalid Choice")

#Create a text file and store student details.
file = open("student.txt", "w")
name = input("Enter student name: ")
marks = input("Enter marks: ")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()


#Read data from a file.
file = open("student.txt", "r")
co = file.read()
print(co)
file.close()

#Handle division by zero using exception handling.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error")

#Create a Student class with name and marks.
class Student:
    def __init__(id, name, marks):
        id.name = name
        id.marks = marks
    def display(id):
        print("Student Name:", id.name)
        print("Marks:", id.marks)
name = input("Enter student name: ")
marks = int(input("Enter marks: "))
s1 = Student(name, marks)
s1.display()

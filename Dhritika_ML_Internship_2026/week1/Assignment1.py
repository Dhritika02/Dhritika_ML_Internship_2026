#Find area of rectangle
a = int(input("Enter length: "))
b = int(input("Enter width: "))
print("Area of  rectangle =", a * b)


#Find simple interest.
p = int(input("Enter Principal: "))
r = int(input("Enter Rate of Interest: "))
t = int(input("Enter Time (years): "))
si = (p * r * t) / 100
print("Simple Interest:", si)


#Convert temperature from Celsius to Fahrenheit.
c = int(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)


#Calculate average of 3 numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
ave = (a + b + c) / 3
print("Average:", ave)


#Find square and cube of a number.
a = float(input("Enter a number: "))
square = a ** 2
cube = a ** 3
print("Square:", square)
print("Cube:", cube)


#Swap two numbers without third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("Swapping:")
print("a =", a)
print("b =", b)


"""Create a Student Report Program that take
student details using input(), Store marks in
variables, Calculate total and percentage ,
Use comments, Use proper indentation"""
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
total = maths + science + english
percentage = (total / 300) * 100
print("Student Report")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
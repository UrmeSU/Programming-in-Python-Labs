Problem 1:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swap:")
print("a =", a)
print("b =", b)


problem 2:
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance =", distance)

problem 3:
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

problem 4:
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Not Vowel")

problem 5:
marks = float(input("Enter marks: "))

if marks >= 80:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 70:
    print("A-")
elif marks >= 65:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 55:
    print("B-")
elif marks >= 50:
    print("C+")
elif marks >= 45:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

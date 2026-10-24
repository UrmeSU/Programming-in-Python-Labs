problem 1:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


problem 2:
num = int(input("Enter a number: "))

while num >= 0:
    print(num)
    num -= 1


problem 3:
base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result *= base

print("Result =", result)


problem 4:
total = 0

for num in range(2, 1000):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        total += num

print("Sum of primes below 1000 =", total)


problem 5: 
N = int(input("Enter N: "))

a, b = 0, 1

while a < N:
    print(a, end=" ")
    a, b = b, a + b

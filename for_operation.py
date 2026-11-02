

#1. Print natural numbers upto n
print("\n1. Print natural numbers upto n")
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i, end=" ")


#2. Print even numbers upto n
print("\n\n2. Print even numbers upto n")
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")


#3. Print odd numbers upto n
print("\n\n3. Print odd numbers upto n")
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 2 != 0:
        print(i, end=" ")


#4. Print 1 2 4 8 16...
print("\n\n4. Print powers of 2")
n = int(input("Enter n: "))
x = 1
for i in range(n):
    print(x, end=" ")
    x *= 2


#5. Sum of series 1 + 1/1! + 1/2! + ... + 1/n!
print("\n\n5. Sum of series")
n = int(input("Enter n: "))
fact = 1
sum = 1
for i in range(1, n+1):
    fact *= i
    sum += 1/fact
print(sum)


#6. Cosine Series
print("\n\n6. Cosine Series")
x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 1
fact = 1
sign = -1
for i in range(2, n+1, 2):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += sign * (x**i)/fact
    sign *= -1
print(sum)


#7. Check square root is prime or not
print("\n\n7. Square root is prime or not")
import math
n = int(input("Enter number: "))
r = int(math.sqrt(n))
prime = True
for i in range(2, r):
    if r % i == 0:
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Not Prime")


#8. Pattern
print("\n\n8. Pattern")
for i in range(3):
    print("A B C")


#9. Pattern
print("\n9. Pattern")
n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()


#10. Pattern
print("\n10. Pattern")
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()


#11. Number Pattern
print("\n11. Pattern")
n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


#12. Number Pattern
print("\n12. Pattern")
n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()

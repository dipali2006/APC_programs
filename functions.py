#Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("Factorial of is:", factorial(num))

#Write a function check_even_odd(n) that determines whether a given number is even or odd.

def even_odd(num):
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

num=int(input("enter the number:"))
even_odd(num)

#Define a function that accepts two numbers and returns the greater number.
def greater(no1,no2):
    if no1>no2:
        print("no 1 is greater")
    else:
        print("no2 is greater")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
greater(num1,num2)


#Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p,r,t):
    si=(p*r*t)/100
    print("simple interest:",si)
principle=int(input("enter the principle:"))
rate=float(input("enter the rate"))
time=int(input("enter the time"))
simple_interest(principle,rate,time)

#Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
no=int(input("enter the number:"))
if is_prime(no):
    print("prime number")
else:
    print("not prime")

#Define a function to calculate the area of a circle using its radius.
def area(r):
    a=3.14*r*r
    print("area:",a)
radius=float(input("enter the radius:"))
area(radius)



#Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_naturals(no):
    s=0
    for i in range(no):
        s=s+i
    print("sum is:",s)
n=int(input("enter the number:"))
sum_naturals(n)

#Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base,exponent):
    p=base**exponent
    print("power=",p)
exp=int(input("enter the exponent:"))
power(10,exp)


#Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def greater_num():
    l1=[]
    n=int(input("enter the number user want"))
    for i in range(n):
        n1=int(input("enter the number:"))
        l1.append(n1)
    greater=l1[0]
    for i in range(n):
        if l1[i] >greater:
            greater=l1[i]

    print("largest number=",greater)

greater_num()


#Define a function that accepts a string and returns the number of vowels present in it
def vowels(str1):
    vowels=0
    for i in str1:
        if i in "AEIOUaeiou":
            vowels+=1
    print("vowels count:",vowels)
str2=input("enter the string:")
vowels(str2)

#Write a function that accepts a string and returns its reverse.
def rev(str1):
    print("reverse string:",str1[::-1])
str2=input("enter the string:")
rev(str2)


#Create a function that checks whether a given string or number is a palindrome.
def palindrome(str1):
    if str1==str1[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome")
str2=input("enter the string")
palindrome(str2)

# Create a function to find the second-largest number in a list.

def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

numbers = [10, 20, 50, 40, 50, 30]
print("Second Largest:", second_largest(numbers))

#  Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_occurrences(lst, element):
    return lst.count(element)

numbers = [1, 2, 3, 2, 4, 2, 5]
print("Occurrences:", count_occurrences(numbers, 2))

#  Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique List:", unique_elements(numbers))

#  Create a function to find the second-largest number in a list.

def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

numbers = [10, 20, 50, 40, 50, 30]
print("Second Largest:", second_largest(numbers))

#  Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("Fibonacci Series:", fibonacci(10))

# Create a function that accepts marks in five subjects and returns the student's percentage and grade.

def student_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade

per, grade = student_result(85, 90, 88, 75, 80)
print("Percentage:", per)
print("Grade:", grade)


#  Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.

def electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + (units - 100) * 2.5
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (units - 300) * 6

    return bill

print("Electricity Bill:", electricity_bill(350))

#  Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def gross_salary(basic):
    hra = basic * 0.20   # 20% HRA
    da = basic * 0.10    # 10% DA
    gross = basic + hra + da
    return gross

basic_salary = 30000
print("Gross Salary:", gross_salary(basic_salary))

# Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def calculate_bill(prices, quantities, discount):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    discount_amount = (total * discount) / 100
    final_bill = total - discount_amount

    return total, discount_amount, final_bill


n = int(input("Enter number of items: "))

prices = []
quantities = []

for i in range(n):
    prices.append(float(input("Enter price: ")))
    quantities.append(int(input("Enter quantity: ")))

discount = float(input("Enter discount (%): "))

total, dis, final = calculate_bill(prices, quantities, discount)

print("Total Bill =", total)
print("Discount =", dis)
print("Final Bill =", final)

# Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def calculate(lst):
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    average = total / len(lst)

    return minimum, maximum, total, average


n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    numbers.append(int(input("Enter number: ")))

mn, mx, total, avg = calculate(numbers)

print("Minimum =", mn)
print("Maximum =", mx)
print("Sum =", total)
print("Average =", avg)

# Write a program using separate functions to process student records containing name, roll number, and marks in five subjects.

def total_marks(marks):
    return sum(marks)

def percentage(total):
    return total / 5

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")

    marks = []
    for j in range(5):
        marks.append(int(input("Enter Marks: ")))

    total = total_marks(marks)
    per = percentage(total)
    g = grade(per)

    students.append([name, roll, total, per, g])

class_total = 0

for s in students:
    class_total += s[3]

print("\nStudent Details")
for s in students:
    print(s)

print("Class Average =", class_total / n)

highest = max(students, key=lambda x: x[2])
lowest = min(students, key=lambda x: x[2])

print("Highest Scorer =", highest[0], highest[2])
print("Lowest Scorer =", lowest[0], lowest[2])



# Create functions for deposit, withdrawal, balance enquiry, and transaction history.

balance = 1000
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited " + str(amount))

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient Balance")

def enquiry():
    print("Balance =", balance)

def transaction_history():
    print("\nTransaction History")
    for i in history:
        print(i)

deposit(500)
withdraw(300)
withdraw(2000)
enquiry()
transaction_history()



# Create functions to add books, issue books, return books, search books, and display available books.

books = {}

def add_book(name):
    books[name] = "Available"

def issue_book(name):
    if name in books and books[name] == "Available":
        books[name] = "Issued"
    else:
        print("Book not available")

def return_book(name):
    if name in books:
        books[name] = "Available"

def search_book(name):
    if name in books:
        print(name, ":", books[name])
    else:
        print("Book not found")

def display_books():
    print("\nAvailable Books")
    for book, status in books.items():
        if status == "Available":
            print(book)

add_book("Python")
add_book("Java")
add_book("C Programming")

issue_book("Python")
return_book("Python")
search_book("Java")
display_books()


# Develop a modular program using functions to calculate electricity bills
# using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_energy_charge(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return 100 * 2 + (units - 100) * 3
    else:
        return 100 * 2 + 100 * 3 + (units - 200) * 5

def fixed_charge():
    return 100

def tax(amount):
    return amount * 0.05

def discount(amount):
    if amount > 1000:
        return amount * 0.10
    return 0

units = int(input("Enter units consumed: "))

energy = calculate_energy_charge(units)
fixed = fixed_charge()
subtotal = energy + fixed
gst = tax(subtotal)
disc = discount(subtotal)

final_bill = subtotal + gst - disc

print("Energy Charge =", energy)
print("Fixed Charge =", fixed)
print("GST =", gst)
print("Discount =", disc)
print("Final Bill =", final_bill)

# Create functions to calculate consultation charges, laboratory charges,
# medicine charges, room charges, and final bill.
# Apply discounts based on patient category.

def consultation():
    return float(input("Enter consultation charge: "))

def laboratory():
    return float(input("Enter laboratory charge: "))

def medicine():
    return float(input("Enter medicine charge: "))

def room():
    return float(input("Enter room charge: "))

def discount(total, category):
    if category.lower() == "senior":
        return total * 0.20
    elif category.lower() == "staff":
        return total * 0.30
    else:
        return 0

c = consultation()
l = laboratory()
m = medicine()
r = room()

category = input("Enter patient category (General/Senior/Staff): ")

total = c + l + m + r
dis = discount(total, category)
final = total - dis

print("Total Bill =", total)
print("Discount =", dis)
print("Final Bill =", final)

# Implement functions to add/remove products, calculate subtotal,
# apply coupon discounts, calculate GST, and generate the final invoice.

cart = []

def add_product(name, price):
    cart.append((name, price))

def remove_product(name):
    global cart
    cart = [item for item in cart if item[0] != name]

def subtotal():


    return sum(price for name, price in cart)

def coupon(total):
    if total >= 1000:
        return total * 0.10
    return 0

def gst(total):
    return total * 0.18

add_product("Mouse", 500)
add_product("Keyboard", 700)
add_product("USB", 300)

remove_product("USB")

sub = subtotal()
dis = coupon(sub)
tax = gst(sub - dis)

final = sub - dis + tax

print("Subtotal =", sub)
print("Discount =", dis)
print("GST =", tax)
print("Final Invoice =", final)

# Write a recursive function to search for an element
# in a sorted list using binary search.

def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)

# Convert a decimal number into binary using recursion
# without using Python's built-in conversion functions.

def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

num = int(input("Enter decimal number: "))

if num == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(num))


# Check whether a string is a palindrome using recursion.

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

string = input("Enter a string: ")

if palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")

# Create separate functions for addition, subtraction,
# multiplication, and division.
# Pass these functions as arguments to another function called calculate().

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

def calculate(fun, a, b):
    return fun(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", calculate(addition, a, b))
print("Subtraction =", calculate(subtraction, a, b))
print("Multiplication =", calculate(multiplication, a, b))
print("Division =", calculate(division, a, b))

# Write a lambda function to calculate the square of a given number.

square = lambda x: x * x

num = int(input("Enter a number: "))
print("Square =", square(num))

# Create a lambda function that returns the cube of a number.

cube = lambda x: x ** 3

num = int(input("Enter a number: "))
print("Cube =", cube(num))
Program
# Write a lambda function that returns True if a number is even and False otherwise.

even = lambda x: x % 2 == 0

num = int(input("Enter a number: "))
print(even(num))

# Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))
Program
# Create a lambda function to calculate simple interest
# using principal, rate, and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest =", simple_interest(p, r, t))
Program
# Take a list of numbers, use map() and a lambda function
# to generate a list containing their squares.

numbers = list(map(int, input("Enter numbers: ").split()))

square = list(map(lambda x: x * x, numbers))

print(square)

# Use map() with lambda to calculate the cube of every element in a list.

numbers = list(map(int, input("Enter numbers: ").split()))

cube = list(map(lambda x: x ** 3, numbers))

print(cube)

# Take two lists of numbers, use map() and lambda to create
# a third list containing the sum of corresponding elements.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda a, b: a + b, list1, list2))

print(result)

# Take a list of integers, use filter() and lambda to extract all even numbers.

numbers = list(map(int, input("Enter numbers: ").split()))

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


# Take a list of integers, use filter() with lambda to identify prime numbers.

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers: ").split()))

primes = list(filter(lambda x: prime(x), numbers))

print(primes)

# Use filter() and lambda to extract positive numbers from a list.

numbers = list(map(int, input("Enter numbers: ").split()))

positive = list(filter(lambda x: x > 0, numbers))

print(positive)


# Take a list of numbers, use filter() and lambda to find numbers greater than 50.

numbers = list(map(int, input("Enter numbers: ").split()))

result = list(filter(lambda x: x > 50, numbers))

print(result)


# Take a list of words, use filter() and lambda to find words having more than five characters.

words = input("Enter words: ").split()

result = list(filter(lambda x: len(x) > 5, words))

print(result)


# Take a list of words; sort them according to their length using lambda.

words = input("Enter words: ").split()

words.sort(key=lambda x: len(x))

print(words)


# Take a list of tuples containing student names and marks,
# sort the students according to their marks using lambda.

students = [("Amit", 78), ("Neha", 92), ("Riya", 65), ("Raj", 85)]

students.sort(key=lambda x: x[1])

print(students)
# Take employee records containing name and salary,
# sort them according to salary using lambda.

employees = [("Amit", 45000), ("Neha", 60000), ("Raj", 52000)]

employees.sort(key=lambda x: x[1])

print(employees)


# Take a list containing student names and marks.
# a) Calculate average marks.
# b) Filter students scoring above 75.
# c) Sort students according to marks.

students = [("Amit", 78), ("Neha", 92), ("Raj", 65), ("Riya", 85)]

average = sum(map(lambda x: x[1], students)) / len(students)

above75 = list(filter(lambda x: x[1] > 75, students))

sorted_students = sorted(students, key=lambda x: x[1])

print("Average =", average)
print("Above 75 =", above75)
print("Sorted =", sorted_students)


# Take employee records containing name, department, and salary.
# a) Find employees earning more than ₹50,000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.

employees = [
    ("Amit", "HR", 45000),
    ("Neha", "IT", 70000),
    ("Raj", "Sales", 55000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

updated_salary = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))

sorted_salary = sorted(employees, key=lambda x: x[2])

print("Salary > 50000 =", high_salary)
print("Updated Salary =", updated_salary)
print("Sorted =", sorted_salary)


# Take a list of products with names, prices, and quantities.
# a) Calculate total value of each product.
# b) Filter products costing more than ₹1000.
# c) Sort products according to total value.

products = [
    ("Pen", 20, 50),
    ("Book", 200, 10),
    ("Bag", 1200, 2)
]

total_value = list(map(lambda x: (x[0], x[1] * x[2]), products))

costly = list(filter(lambda x: x[1] > 1000, products))

sorted_products = sorted(products, key=lambda x: x[1] * x[2])

print("Total Value =", total_value)
print("Costly Products =", costly)
print("Sorted =", sorted_products)

# Write a program using functions, map(), filter(), and lambda expressions
# to process a list of words.
# a) Find the length of every word.
# b) Extract words having more than five characters.
# c) Sort the words according to their length.

words = input("Enter words: ").split()

lengths = list(map(lambda x: len(x), words))

long_words = list(filter(lambda x: len(x) > 5, words))

sorted_words = sorted(words, key=lambda x: len(x))

print("Lengths =", lengths)
print("Words > 5 characters =", long_words)
print("Sorted =", sorted_words)


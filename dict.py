

# 1.Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
students={"Name":"Dipali","roll_no":143,"department":"CSE","marks":97}
print(students)


# 2. Create a dictionary containing employee information and display the value associated with a specified key.

emp = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}

key = input("Enter key: ")

if key in emp:
    print(emp[key])
else:
    print("Key not found")

# 3. Create a dictionary of five products and their prices.
# Add a new product and price to the dictionary.

products = {
    "Pen": 10,
    "Book": 100,
    "Bag": 500,
    "Bottle": 150,
    "Pencil": 5
}

name = input("Enter new product: ")
price = int(input("Enter product price: "))

products[name] = price

print("Updated Dictionary:")
print(products)

# 4. Create a dictionary containing student marks.
# Update the marks of a specified student.

marks = {
    "Amit": 80,
    "Neha": 90,
    "Riya": 85
}

name = input("Enter student name: ")

if name in marks:
    marks[name] = int(input("Enter new marks: "))
    print("Updated Dictionary:")
    print(marks)
else:
    print("Student not found")


# 5. Create a dictionary of cities and their populations.
# Remove a specified city from the dictionary.

cities = {
    "Kolhapur": 550000,
    "Pune": 7000000,
    "Mumbai": 12000000,
    "Sangli": 300000
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("City removed successfully.")
else:
    print("City not found.")

print(cities)


# 6. Create a dictionary of employee IDs and names.
# Ask the user for an employee ID and check whether it exists.

employees = {
    101: "Amit",
    102: "Neha",
    103: "Riya",
    104: "Rahul"
}

eid = int(input("Enter Employee ID: "))

if eid in employees:
    print("Employee Name:", employees[eid])
else:
    print("Employee ID not found.")

# 7. Create a dictionary containing student records and find
# the total number of key-value pairs.

students = {
    "Amit": 85,
    "Neha": 90,
    "Riya": 78,
    "Rahul": 88
}

print("Total key-value pairs:", len(students))

# 8. Create a dictionary and display:
# All keys
# All values
# All key-value pairs

student = {
    "Name": "Amit",
    "Age": 20,
    "Marks": 85
}

print("Keys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# 9. Create a dictionary of programming languages and their creators.
# Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}

for key, value in languages.items():
    print(key, "->", value)


# 10. Accept five student names and their marks from the user
# and store them in a dictionary.

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Dictionary:")
print(students)

# 11. Create a dictionary containing student names and marks.
# Find the student who has scored the highest marks.

students = {
    "Amit": 85,
    "Neha": 92,
    "Riya": 78,
    "Rahul": 88
}

name = max(students, key=students.get)

print("Highest Scorer:", name)
print("Marks:", students[name])


# 12. Create a dictionary containing student names and marks.
# Find the student with the lowest marks.

students = {
    "Amit": 85,
    "Neha": 92,
    "Riya": 78,
    "Rahul": 88
}

name = min(students, key=students.get)

print("Lowest Scorer:", name)
print("Marks:", students[name])

# 13. Create a dictionary containing student names and marks.
# Calculate the average marks of all students.

students = {
    "Amit": 85,
    "Neha": 92,
    "Riya": 78,
    "Rahul": 88
}

total = sum(students.values())
average = total / len(students)

print("Average Marks:", average)


# 14. Accept a string from the user and create a dictionary
# containing each character and its frequency.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)


# 15. Accept a sentence and create a dictionary containing
# each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)


# 16. Create two dictionaries and merge them into a single dictionary.

dict1 = {
    "A": 10,
    "B": 20
}

dict2 = {
    "C": 30,
    "D": 40
}

dict1.update(dict2)

print("Merged Dictionary:")
print(dict1)


# 17. Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "B": 50,
    "C": 60,
    "D": 70
}

print("Common Keys:")

for key in dict1:
    if key in dict2:
        print(key)


# 18. Given two dictionaries, identify the values that are common to both dictionaries.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "X": 20,
    "Y": 40,
    "Z": 30
}

print("Common Values:")

for value in dict1.values():
    if value in dict2.values():
        print(value)


# 19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

new_dict = {}

for key, value in data.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Dictionary after removing duplicate values:")
print(new_dict)


# 20. Create a dictionary and display its elements in ascending order of keys.

student = {
    "C": 85,
    "A": 95,
    "D": 78,
    "B": 90
}

print("Dictionary in Ascending Order:")

for key in sorted(student):
    print(key, ":", student[key])

    

# 21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.

numbers = {}

for i in range(1, 11):
    numbers[i] = i * i


# 22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values,
# but include only even numbers.

numbers = {}

for i in range(2, 21, 2):
    numbers[i] = i * i

print(numbers)


# 23. Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [1, 2, 3, 2, 4, 1, 3, 2, 5]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


# 24. Create a dictionary containing integers from 1 to 10 and their cubes.

cube = {}

for i in range(1, 11):
    cube[i] = i ** 3

print(cube)


# 25. Create a dictionary containing student names and marks.
# Develop a program to:
# Add a student
# Update marks
# Delete a student
# Search for a student
# Display all students
# Find the highest marks
# Calculate the average

students = {
    "Amit": 85,
    "Neha": 90,
    "Riya": 80
}

# Add a student
students["Rahul"] = 88

# Update marks
students["Amit"] = 95

# Delete a student
del students["Riya"]

# Search for a student
name = input("Enter student name to search: ")

if name in students:
    print(name, "Marks:", students[name])
else:
    print("Student not found.")

# Display all students
print("\nStudent Records:")
for key, value in students.items():
    print(key, ":", value)

# Find highest marks
highest = max(students, key=students.get)

print("\nHighest Scorer:", highest)
print("Marks:", students[highest])

# Calculate average
total = sum(students.values())
average = total / len(students)

print("Average Marks:", average)

print(numbers)



# 26. Create a dictionary containing employee names and salaries.
# Find:
# • Highest salary
# • Lowest salary
# • Average salary
# • Employees earning more than ₹50,000

employees = {
    "Amit": 45000,
    "Neha": 60000,
    "Rahul": 75000,
    "Riya": 52000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


# 27. Create a dictionary containing product names and quantities.
# Perform:
# • Add a product
# • Update quantity
# • Delete a product
# • Search for a product
# • Display products with quantity below 10

products = {
    "Pen": 20,
    "Book": 8,
    "Bag": 15
}

# Add product
products["Bottle"] = 12

# Update quantity
products["Pen"] = 25

# Delete product
del products["Bag"]

# Search product
name = input("Enter product name: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("\nProducts with quantity below 10:")
for product, qty in products.items():
    if qty < 10:
        print(product, ":", qty)


# 28. Create a dictionary containing names and phone numbers.
# Implement:
# • Add contact
# • Search contact
# • Update contact
# • Delete contact
# • Display all contacts

contacts = {
    "Amit": "9876543210",
    "Neha": "9123456789",
    "Riya": "9988776655"
}

# Add contact
contacts["Rahul"] = "9871234567"

# Search contact
name = input("Enter contact name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact not found")

# Update contact
contacts["Amit"] = "9999999999"

# Delete contact
del contacts["Riya"]

print("\nAll Contacts:")
for name, number in contacts.items():
    print(name, ":", number)


# 29. Create a dictionary containing book IDs and book names.
# Implement:
# • Add a book
# • Search a book
# • Remove a book
# • Display all books
# • Count total books

books = {
    101: "Python",
    102: "Java",
    103: "C Programming"
}

# Add book
books[104] = "Data Structures"

# Search book
book_id = int(input("Enter Book ID: "))

if book_id in books:
    print("Book Name:", books[book_id])
else:
    print("Book not found")

# Remove book
del books[102]

print("\nBook List:")
for bid, name in books.items():
    print(bid, ":", name)

print("Total Books:", len(books))



# 30. Take a dictionary containing student names and their departments.
# Create a new dictionary that groups students according to their department.

students = {
    "Amit": "CSE",
    "Neha": "IT",
    "Riya": "CSE",
    "Rahul": "ECE",
    "Pooja": "IT"
}

group = {}

for name, dept in students.items():
    if dept not in group:
        group[dept] = []

    group[dept].append(name)

print(group)



# 31. Take a list of words.
# Create a dictionary where the key is the word length
# and the value is a list of words having that length.

words = ["apple", "bat", "cat", "banana", "dog", "orange"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)


# 32. Take a list of integers and a target value.
# Find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15]

target = int(input("Enter target value: "))

data = {}

for num in numbers:
    difference = target - num

    if difference in data:
        print("Numbers are:", difference, "and", num)
        break

    data[num] = True



# 33. Take a string.
# Use a dictionary to find the first character that occurs only once.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break


# 34. Take a string.
# Use a dictionary to find the first character that occurs more than once.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break

# 35. Accept a paragraph and create a dictionary where:
# • Key = word length
# • Value = number of words having that length.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()

result = {}

for word in words:
    length = len(word)

    if length in result:
        result[length] += 1
    else:
        result[length] = 1

print(result)

          




















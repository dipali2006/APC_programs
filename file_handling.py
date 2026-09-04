# Program 1: Create a file and write student details

with open("student.txt", "w") as file:
    file.write("Name: Dipali Kolekar\n")
    file.write("Roll No: 143\n")
    file.write("Branch: CSE\n")
    file.write("Semester: 3\n")

print("Student details written successfully.")


# Program 2: Open a text file and display its complete contents

with open("student.txt", "r") as file:
    content = file.read()

print(content)


# Program 3: Append additional student information

with open("student.txt", "a") as file:
    file.write("College: DYP College of Engineering\n")
    file.write("City: Kolhapur\n")

print("Data appended successfully.")


# Program 4: Read a text file line by line

with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")


# Program 5: Count the total number of lines

count = 0

with open("student.txt", "r") as file:
    for line in file:
        count += 1

print("Total Lines =", count)


# Program 6: Count the total number of words

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total Words =", len(words))


# Program 7: Count the total number of characters including spaces

with open("student.txt", "r") as file:
    content = file.read()

print("Total Characters =", len(content))


# Program 8: Display the lines of a file in reverse order

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end="")


# Program 9: Count the number of vowels and consonants

vowels = 0
consonants = 0

with open("student.txt", "r") as file:
    content = file.read().lower()

for ch in content:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)


# Program 10: Count alphabets, digits, spaces, and special characters

alphabets = 0
digits = 0
spaces = 0
special = 0

with open("student.txt", "r") as file:
    content = file.read()

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets =", alphabets)
print("Digits =", digits)
print("Spaces =", spaces)




# Program 11: Read a text file and find the longest word

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()
longest = max(words, key=len)

print("Longest Word =", longest)


# Program 12: Count how many times each word occurs using a dictionary

with open("student.txt", "r") as file:
    content = file.read().lower()

words = content.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("Word Frequency:")
for key, value in count.items():
    print(key, ":", value)


# Program 13: Search for a word and display occurrences and line numbers

word = input("Enter word to search: ").lower()

count = 0

with open("student.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    if word in line.lower():
        count += line.lower().count(word)
        print("Found in Line", i)

print("Total Occurrences =", count)


# Program 14: Replace a specified word with another word

old = input("Enter word to replace: ")
new = input("Enter new word: ")

with open("student.txt", "r") as file:
    content = file.read()

content = content.replace(old, new)

with open("student.txt", "w") as file:
    file.write(content)

print("Word replaced successfully.")


# Program 15: Remove single-line comments from a Python source file

with open("input.py", "r") as file:
    lines = file.readlines()

with open("output.py", "w") as file:
    for line in lines:
        if not line.strip().startswith("#"):
            file.write(line)

print("Comments removed successfully.")


# Program 16: Create another file containing uppercase text

with open("student.txt", "r") as file:
    content = file.read()

with open("uppercase.txt", "w") as file:
    file.write(content.upper())

print("Uppercase file created successfully.")


# Program 17: Student record operations

with open("students.txt", "r") as file:
    lines = file.readlines()

print("Student Records:")
for line in lines:
    print(line.strip())

highest = 0
name = ""
total = 0
count = 0

for line in lines:
    if line.startswith("RollNo"):
        continue

    data = line.strip().split(",")
    marks = int(data[2])

    total += marks
    count += 1

    if marks > highest:
        highest = marks
        name = data[1]

print("Highest Marks =", highest)
print("Topper =", name)
print("Average Marks =", total / count)

print("Students Scoring More Than 80:")
for line in lines:
    if line.startswith("RollNo"):
        continue

    data = line.strip().split(",")
    if int(data[2]) > 80:
        print(data[1], data[2])


# Program 18: Employee record operations

with open("employee.txt", "r") as file:
    lines = file.readlines()

highest = 0
name = ""
total = 0
count = 0

salary_limit = int(input("Enter salary limit: "))

print("Employee Records:")
for line in lines:
    print(line.strip())

for line in lines:
    data = line.strip().split(",")
    salary = int(data[3])

    total += salary
    count += 1

    if salary > highest:
        highest = salary
        name = data[1]

print("Highest Paid Employee =", name)
print("Highest Salary =", highest)
print("Average Salary =", total / count)

print("Employees earning above", salary_limit)

for line in lines:
    data = line.strip().split(",")
    if int(data[3]) > salary_limit:
        print(data[1], data[3])


# Program 19: Calculate attendance percentage

with open("attendance.txt", "r") as file:
    lines = file.readlines()

print("Students with Attendance Below 75%")

for line in lines:
    data = line.strip().split(",")

    name = data[0]
    attended = int(data[1])
    total = int(data[2])

    percentage = (attended / total) * 100

    print(name, "Attendance =", percentage)

    if percentage < 75:
        print(name, "is below 75% attendance.")


# Program 20: Calculate banking transactions

with open("transactions.txt", "r") as file:
    lines = file.readlines()

deposits = 0
withdrawals = 0
balance = 0
largest = 0

for line in lines:
    data = line.strip().split(",")

    ttype = data[0]
    amount = int(data[1])

    if amount > largest:
        largest = amount

    if ttype.lower() == "deposit":
        deposits += amount
        balance += amount
    else:
        withdrawals += amount
        balance -= amount

print("Total Deposits =", deposits)
print("Total Withdrawals =", withdrawals)
print("Final Balance =", balance)
print("Largest Transaction =", largest)


# Program 21: Book record operations

books = {}

while True:
    print("\n1.Add Book")
    print("2.Search Book")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Display Available Books")
    print("6.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        bid = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        books[bid] = [title, author, "Available"]

    elif ch == 2:
        bid = input("Enter Book ID: ")
        if bid in books:
            print(books[bid])
        else:
            print("Book Not Found")

    elif ch == 3:
        bid = input("Book ID: ")
        if bid in books:
            books[bid][2] = "Issued"

    elif ch == 4:
        bid = input("Book ID: ")
        if bid in books:
            books[bid][2] = "Available"

    elif ch == 5:
        for bid, data in books.items():
            if data[2] == "Available":
                print(bid, data)

    elif ch == 6:
        break


# Program 22: Merge two text files into a third file

with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("file3.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

print("Files merged successfully.")


# Program 23: Compare two text files

with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()

with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")

    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("First difference at Line", i + 1)
            print("File1:", lines1[i].strip())
            print("File2:", lines2[i].strip())
            break




    
print("Special Characters =", special)

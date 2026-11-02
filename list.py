list1=["apple","banana","cherry","mango"]
print(list1)

#Q2
list1=[10,40,37,57,26]
print(list1[0])
print(list1[2])
print(list1[-1])


#Q3
list1=["red","blue","skyblue","pink","black","white"]
print(list1)
list1[2]="gray"
print(list1)

#q4
#Create a list of numbers. Add:
#One element at the end 
#One element at the beginning 
#One element at a specified position 
#Display the updated list.

list1=[10,20,30,40]
list1.insert(0,9)
list1.append(50)
list1.insert(4,60)
print(list1)

#Create a list of student names. Remove:
#First student 
#Last student 
#A specific student by name 
#Display the remaining list.


list1=["joy","dipali","sayali","sanika","shreya"]
list1.remove("joy")
list1.pop()
list1.remove("sayali")
print(list1)


#6.Write a program to find the largest and smallest number in a list without using max() or min().

list1=[32,45,36,78,34]
smallest=list1[0]
for i in range(len(list1)):
    if list1[i]<smallest:
        smallest=list1[i]
print(smallest)

list1=[32,45,36,78,34]
largest=list1[0]
for i in range(len(list1)):
    if list1[i]>largest:
        largest=list1[i]
print(largest)


#Accept 10 numbers from the user and store them in a list. Calculate:
#Sum 
#Average

numbers = []

for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
print("Numbers:", numbers)
print("Sum =", total)
print("Average =", average)
#even odd

numbers = []

for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)

#Count Even and Odd Numbers
numbers = []

for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)

# Search City
cities = ["Pune", "Mumbai", "Kolhapur", "Sangli", "Satara"]

city = input("Enter city name: ")

if city in cities:
    print("City found")
else:
    print("City not found")
    
# Reverse List without reverse()
lst = [10, 20, 30, 40, 50]

rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print(rev)

#List Slicing
lst = [10,20,30,40,50,60,70,80,90,100]

print("First 5:", lst[:5])
print("Last 5:", lst[-5:])
print("Middle 4:", lst[3:7])
print("Alternate:", lst[::2])
print("Reverse:", lst[::-1])

# Elements at Even Index
lst = [10,20,30,40,50,60,70]

for i in range(0, len(lst), 2):
    print(lst[i])
    
#Sort List
numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

#Display Unique Elements
lst = [10,20,30,20,40,30,50]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)

#Second Largest Element
lst = [10,50,30,80,60]

lst.sort()

print("Second Largest =", lst[-2])

#Nested List Student Details
students = [
    ["Dipali",101,90],
    ["Rahul",102,85],
    ["Priya",103,88]
]

for s in students:
    print("Name:", s[0])
    print("Roll:", s[1])
    print("Marks:", s[2])
    
# Matrix Addition
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

C = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j]+B[i][j])
    C.append(row)

print(C)

#Shopping Cart
cart=[]

cart.append("Milk")
cart.append("Bread")
cart.append("Rice")

print(cart)

cart.remove("Bread")

print(cart)

print("Milk" in cart)

print("Total Items =",len(cart))

# Student Attendance
students=["Amit","Rahul","Priya"]

print("Total Students:",len(students))

name=input("Enter student name: ")

if name in students:
    print("Present")
else:
    print("Absent")

students.append("Dipali")
students.remove("Rahul")

print(students)

#Book List
books=["Python","Java","C"]

books.append("HTML")

print("Books:",books)

book=input("Search Book:")

if book in books:
    print("Available")

books.remove("Java")

print("Total Books:",len(books))

# Merge Two Lists
list1=[1,2,3]
list2=[4,5,6]

list3=list1+list2

print(list3)


#Common Elements
a=[10,20,30,40]
b=[20,40,60]

for i in a:
    if i in b:
        print(i)
        
#Frequency of Elements
lst=[10,20,10,30,20,10]

for i in lst:
    print(i,"=",lst.count(i))
    
# Rotate List
lst=[10,20,30,40,50]

left=lst[1:]+lst[:1]
right=lst[-1:]+lst[:-1]

print("Left:",left)
print("Right:",right)

#Remove Duplicates
lst=[1,2,2,3,4,3,5]

new=[]

for i in lst:
    if i not in new:
        new.append(i)

print(new)

#Student Marks Analysis
marks=[]

for i in range(20):
    marks.append(int(input("Enter Marks: ")))

avg=sum(marks)/len(marks)

print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Average:",avg)

above=0
below=0

for i in marks:
    if i>avg:
        above+=1
    elif i<avg:
        below+=1

print("Above Average:",above)
print("Below Average:",below)

#Employee Salary Analysis
salary=[]

for i in range(5):
    salary.append(int(input("Enter Salary: ")))

print("Highest:",max(salary))
print("Lowest:",min(salary))
print("Average:",sum(salary)/len(salary))

above=0
below=0

for s in salary:
    if s>50000:
        above+=1
    if s<30000:
        below+=1

print("Above 50000:",above)
print("Below 30000:",below)

#Batsman Score Analysis
score=[]

for i in range(10):
    score.append(int(input("Enter Score: ")))

print("Highest:",max(score))
print("Lowest:",min(score))
print("Total:",sum(score))
print("Average:",sum(score)/10)

century=0
half=0

for s in score:
    if s>=100:
        century+=1
    elif s>=50:
        half+=1

print("Centuries:",century)
print("Half Centuries:",half)

# Temperature Analysis
temp=[]

for i in range(30):
    temp.append(float(input("Enter Temperature: ")))

avg=sum(temp)/30

print("Highest:",max(temp))
print("Lowest:",min(temp))
print("Average:",avg)

above=0
below=0

for t in temp:
    if t>avg:
        above+=1
    elif t<avg:
        below+=1

print("Above Average:",above)
print("Below Average:",below)

#Patient List
patients=["Amit","Rahul"]
ages=[25,40]

patients.append("Dipali")
ages.append(21)

name=input("Search Patient:")

if name in patients:
    print("Patient Found")

patients.remove("Rahul")

print("Patients:",patients)

print("Total Patients:",len(patients))





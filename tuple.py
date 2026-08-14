"""#Write a Python program to create a tuple of five integers and display it.
t1=(10,20,30,40,50)
print(t1)

#Create a tuple containing five city names. Display:
#First city 
#Last city 
#Third city
t1=("mumbai","pune","kolhapur","tamilnadu","sangli")
print("first city",t1[0])
print("last city",t1[-1])
print("third city",t1[2])

#Create a tuple of student names and display the total number of students using the len() function.
t1=("dipali","shreya","manasi","sayali","anushaka")
print(len(t1))

#Create a tuple of colors. Check whether a given color exists in the tuple
t1=("red","blue","black","white")
color=input("enter the color=")
for i in t1:
    if i==color:
        print("color exist in tuple")
   

#Create a tuple of fruits and display each fruit using a loop.
t1=("apple","banana","cherry","mango","orange")
for i in t1:
    print(i)

#Create a tuple with repeated numbers and count how many times a particular number appears.
numbers = (1, 2, 3, 2, 4, 2, 5, 3, 1)
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


#Create a tuple of employee IDs and find the index of a given ID.
t1=(101,103,102,402,456,234,789)
id=int(input("enter the id"))
print("index of id",t1.index(id))

#Create two tuples of numbers and concatenate them into a single tuple.
t1=(10,20,30,40)
t2=(50,60,70,80)
t3=t1+t2
print("tuple",t3)

#Create a tuple containing three elements and repeat it four times.
t1=(10,20,30,40)
print(t1*3)

Create a tuple of 10 numbers and display:
First five elements 
Last five elements 
Middle four elements 
Alternate elements 
Reverse tuple

t1=(10,20,30,40,50,60,70,80,90,100)
print("first five elements",t1[:5])
print("last five element",t1[5:])
print("middle four elements",t1[2:5])
print("alternative elements",t1[::2])
print("reverse tuple",t1[::-1])

#Convert a tuple into a list and add a new element.
t1=(10,20,30,40,50)
l1=list(t1)
l1.append(60)
print(l1)

#Accept five numbers from the user, store them in a list, and convert the list into a tuple.
num=int(input("enter number you wnat to accept:"))
ls=[]
for i in range(num):
    no=int(input("enter the numbers:"))
    ls.append(no)
t1=tuple(ls)
print(t1)

#Modify a tuple by converting it into a list and then back into a tuple.
t1=(10,20,30,40,50)
l1=list(t1)
l1.append(60)
print("first tuple",t1)
print("list elements",l1)
t2=tuple(l1)
print("second tuple",t2)


#Create a tuple and delete it completely.
t1=(10.20,30,40,50)
del t1
print("deleted sucessfully")


#Create a nested tuple containing student details and display each record.
t1=((101,"dipali"),(102,"sayali"),(103,"shreya"))
for i in t1:
    print(i)


#Store ten numbers in a tuple and calculate their sum.
t1=(10.20,30,40,50,60,70,80,90,100)
sum1=sum(t1)
print(sum1)

#Find the largest and smallest number in a tuple without using max() and min().
t1=(10,20,30,56,32)
large=t1[0]
small=t1[0]
for i in t1:
    if i >large:
        large=i
    elif i<small:
        small=i
print("largest element",large)
print("smallest element",small)

#Calculate the average of elements stored in a tuple.
t1=(10,20,30,56,32)
avg=sum(t1)/len(t1)
print("avarage of tuple",avg)



#Store 15 integers in a tuple and count:
#Even numbers 
#Odd numbers
t1=(23,45,23,67,23,56,43,16,79,45,23,67,90,34,56)
even=0
odd=0
for i in t1:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even count",even)
print("odd count",odd)

#Accept a number from the user and determine whether it exists in the tuple.
t1=(10,20,30,40,50)
no=int(input('enter the number'))
if no in t1:
    print("number is exit")
else:
     print("number is not exit")

#Store student details in a tuple:
#Roll Number 
#Name 
#Department 
#marks 
students=((101,"dipali","CSE",91),(102,"sayali","CSE",54))
print(students)

Display all the details.
Create tuples containing:
Employee ID 
Name 
Salary """
"""employee=((101,"dipali",20000)(102,"sayali",342356))
print(employee)"""


"""Store item prices in a tuple and calculate:
Total bill 
Average price 
Highest-priced item 
Lowest-priced item"""
prices=(234,456,321,678,345)
print("total bill",sum(prices))
print("avarage price",sum(prices)/len(prices))
lowest_price=prices[0]
highest_price=prices[0]
for i in prices:
    if i <lowest_price:
        lowest_price=i
    elif i>highest_price:
        highest_price=i 
print("highest price",highest_price)
print("lowest price",lowest_price)

"""Store temperatures of seven days in a tuple and determine:
Maximum temperature 
Minimum temperature 
Average temperature """
temp=(28,34,12,56,34,67,90)
print("minimum temp ",min(temp))
print("maximum temp",max(temp))
print("avarage temp",sum(temp)/len(temp))

"""Store runs scored in 10 matches and calculate:
Total runs 
Highest score 
Lowest score 
Average score """
match=(10,20,30,450,50,60)
print("total score",sum(match))
print("minimum score ",min(match))
print("maximum score",max(match))
print("avarage score",sum(match)/len(match))


#Create two tuples and find the common elements between them.
t1=(10,34,23,56,45,78)
t2=(23,56,34,56,78,89)
for i in t1:
    for j in t2:
        if i==j:
            print(i)


#Merge two tuples and remove duplicate elements.
t1=(10,20,30,40,50)
t2=(45,32,45,34,50)
merged=tuple(set(t1+t2))
print(merged)

#Convert a tuple into a sorted tuple in ascending and descending order.
t1=(32,45,67,45,34,23)
l1=list(t1)
sorted(l1)
t2=tuple(l1)
print(t2)











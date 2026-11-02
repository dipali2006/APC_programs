#write a program to create a set containing five integers and display all its element
s1={10,20,30,40,50}
print(s1)

#Create a list containing duplicate values. Convert the list into a set and display the resulting set.
l1=[10,20,30,10,40,50]
s1=set(l1)
print(s1)

#Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
s1={"apple","banana","cherry"}
s1.add("dragaon fruit")
s1.add(" fruit")
print(s1)

#Create a set of numbers and remove a specified number from the set.
s1={10,20,30,40,50}
s1.remove(50)
print(s1)

#Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
name={"dipali","shreya","sayali"}
names=input("enter the name:")
if names in name:
    print("name exist")
else:
    print("name not exist")


#Create a set of cities and determine the total number of cities using an appropriate function.
cities={"nagapur","kolhapur","sangli","satara"}
print(len(cities))

#Create a set of programming languages and display each language using a for loop.
lang={"marathi","hindi","kanada","telagu"}
for i in lang:
    print("language=",i)



#Create a list containing duplicate numbers, use a set to remove the duplicates.
l1=[10,20,30,40,2,42,3,20]
s1=set(l1)
print(s1)

#Create two sets of integers and find their union.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
uni=s1.union(s2)
print(uni)

#Create two sets and find the elements common to both sets.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
common=s1.intersection(s2)
print(common)

"""
Create two sets and find:
Elements present in the first set but not the second
Elements present in the second set but not the first"""
s1={10,20,30,40,50}
s2={20,40,50,60,40}
print("present in the first set but not in second",s1.difference(s2))
print("present in the second set but not in first",s2.difference(s1))


print#Create two sets of numbers and find the elements that are present in either set but not in both.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
result = s1 ^ s2
print("Elements present in either set but not in both:", result)


#Create two sets and determine whether the first set is a subset of the second set.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
print("first set is subset of second set",s1.issubset(s2))


##Create two sets and determine whether the first set is a supersetset of the second set.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
print("first set is supersetset of second set",s1.issuperset(s2))


#Write a program to determine whether two sets have no elements in common.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
if s1.isdisjoint(s2):
    print("The two sets have no elements in common.")
else:
    print("The two sets have common elements.")

#Create two sets and check whether they are equal.
s1={10,20,30,40,50}
s2={20,40,50,60,40}
if s1==s2:
    print("sets are equal")
else:
    print("sets are not equal")
    

#Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
s1={"marathi","hindi","maths","physics"}
s2={"AJT","PYTHON","JAVA","marathi"}
common=s1.intersection(s2)
print(common)


#Accept a sentence from the user and use a set to display all unique words.
sen=input("enter the sentence")
s1=set(sen)
for i in s1:
    print("wrods=",i)

"""19.	Create two sets:
	Students present in the morning session 
	Students present in the afternoon session 
Find:
	Students present in both sessions 
	Students present only in the morning 
	Students present only in the afternoon 
	Students present in at least one session"""
morning = {"Amit", "Priya", "Rohan", "Sneha"}
afternoon = {"Priya", "Sneha", "Rahul", "Neha"}

print("Students present in both sessions:", morning & afternoon)
print("Students present only in the morning:", morning - afternoon)
print("Students present only in the afternoon:", afternoon - morning)
print("Students present in at least one session:", morning | afternoon)


"""Create sets representing students enrolled in:
	Python 
	Java
Find students enrolled in both courses and students enrolled in only one course."""

python = {"Amit", "Priya", "Rohan", "Sneha"}
java = {"Priya", "Rahul", "Sneha", "Neha"}

print("Students enrolled in both courses:", python & java)
print("Students enrolled in only one course:", python ^ java)


"""Create two sets representing technical skills of two employees. Find:
	Common skills 
	Skills unique to Employee 1 
	Skills unique to Employee 2 
	All available skills"""

emp1 = {"Python", "Java", "SQL", "HTML"}
emp2 = {"Python", "C++", "SQL", "CSS"}

print("Common skills:", emp1 & emp2)
print("Skills unique to Employee 1:", emp1 - emp2)
print("Skills unique to Employee 2:", emp2 - emp1)
print("All available skills:", emp1 | emp2)


#Create a set containing available books and another set containing requested books. Determine which requested books are available.
available = {"Python", "Java", "C", "C++"}
requested = {"Java", "Python", "HTML"}

print("Requested books available:", available & requested)


""" Store visitor IDs from two different days in separate sets. Determine:
	Unique visitors across both days 
	Returning visitors 
	Visitors who came only on the first day 
	Visitors who came only on the second day
	Create sets representing products belonging to different categories. Find products that belong to both categories."""

day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print("Unique visitors across both days:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Visitors only on the first day:", day1 - day2)
print("Visitors only on the second day:", day2 - day1)



"""Represent the friends of two users using sets. Find:
	Mutual friends 
	Friends unique to User 1 
	Friends unique to User 2
	Total unique friends"""


user1 = {"Amit", "Priya", "Rohan", "Sneha"}
user2 = {"Priya", "Sneha", "Rahul", "Neha"}

print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)


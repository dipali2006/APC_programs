
# ==========================================
# Program 7 : Math Utilities Package
# ==========================================
from mypackage.basic import *

from mypackage.number import *
from mypackage.statistics import *

print("----- Math Utilities -----")
print("Addition =", add(10,20))
print("Subtraction =", sub(20,10))
print("Multiplication =", mul(10,5))
print("Division =", div(20,5))

n=int(input("Enter Number : "))
print("Prime =", prime(n))
print("Armstrong =", armstrong(n))
print("Palindrome =", palindrome(n))

lst=[10,20,30,40,50]
print("Mean =", mean(lst))
print("Maximum =", maximum(lst))
print("Minimum =", minimum(lst))


# ==========================================
# Program 8 : Student Package
# ==========================================

from mypackage.marks import *
from mypackage.grade import *
from mypackage.attendance import *

m1=int(input("Enter Marks1 : "))
m2=int(input("Enter Marks2 : "))
m3=int(input("Enter Marks3 : "))

t=total(m1,m2,m3)
p=percentage(t)

print("Total =",t)
print("Percentage =",p)
print("Grade =",grade(p))

att=int(input("Attended Classes : "))
totalcls=int(input("Total Classes : "))

print("Attendance =",eligible(att,totalcls))


# ==========================================
# Program 9 : Banking Package
# ==========================================

from mypackage.account import *
from mypackage.transaction import *
from mypackage.loan import *

showbalance()

bal=10000

amt=int(input("Enter Deposit Amount : "))
bal=deposit(bal,amt)
print("Balance After Deposit =",bal)

amt=int(input("Enter Withdraw Amount : "))
bal=withdraw(bal,amt)
print("Balance After Withdrawal =",bal)

p=int(input("Principal : "))
r=float(input("Rate : "))
t=int(input("Time : "))

print("Simple Interest =",interest(p,r,t))


# ==========================================
# Program 10 : TextTools Package
# ==========================================

from mypackage.cleaning import *
from mypackage.tokenization import *
from mypackage.frequency import *

text=input("Enter Text : ")

cleantext=clean(text)

print("Clean Text =",cleantext)
print("Tokens =",tokenize(cleantext))
print("Frequency =",frequency(cleantext))


# ==========================================
# Program 11 : College Project
# ==========================================

from mypackage.student import *
from mypackage.faculty import *

student_details()
marks()
faculty_details()


# ==========================================
# Program 12 : Library Project
# ==========================================

from mypackage.books import *
from mypackage.members import *
from mypackage.transactions import *

addbook()
addmember()
issuebook()


# ==========================================
# Program 13 : Ecommerce Project
# ==========================================

from mypackage.products import *
from mypackage.customers import *
from mypackage.orders import *
from mypackage.payments import *

product()
customer()
order()
payment()


# ==========================================
# Program 14 : Hospital Project
# ==========================================

from mypackage.patient import *
from mypackage.doctor import *
from mypackage.billing import *
from mypackage.records import *

patient()
doctor()
bill()
records()



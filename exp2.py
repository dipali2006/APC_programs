
#number is even or odd
num=int(input("enter the number:"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")
print("\n")

#number is zero or non zero
n=int(input("enter the number:"))
if n>0:
    print("number is non zero")
else:
    print("number is zero")
    
print("\n")
    
#largest in 2 numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1>num2:
    print("number 1 is largest")
else:
    print("number 2 is largest")
print("\n")

#check number is positive or negative
no=int(input("enter the number:"))
if no>0:
    print("number is positive")
elif no<0:
    print("number is negative")
else:
    print("number is zero")
print("\n")

#character vowel or not
ch=input("enter the character in lowercase:")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("character is vowel")
else:
    print("character is not vowel")
print("\n")


#elif statements
marks=int(input("enter the marks:"))
if marks>=90:
    print("Excellent performance")
elif marks>=80:
    print("Very Good performance")
elif marks>=70:
    print("Good performance")
elif marks>=60:
    print("average performance")
else:
    print("poor performance")
print("\n")

#largest in 3 numbers
no1=int(input("enter the first number:"))
no2=int(input("enter the second number:"))
no3=int(input("enter the third number:"))

if no1>no2:
    print("number 1 is largest")
elif no2>no3:
    print("number 2 is largest")
else:
    print("number 3 is largest")
print("\n")

#smallest in three numbers
o1=int(input("enter the first number:"))
o2=int(input("enter the second number:"))
o3=int(input("enter the third number:"))

if o1<o2:
    print("number 1 is smallest")
elif o2<o3:
    print("number 2 is smallest")
else:
    print("number 3 is smallest")
print("\n")

#check the year is leap
year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("lear year")
else:
    print("not leap year")
    
print("\n")

#driver issued the licences
status=input("enter the status married or unmarried:")
age1=int(input("enter the age:"))
gender=input("enter the gender male or female:")
if status=='married':
    print("driver is insured :")
elif status=='unmarried' and age1>30 and gender=='male':
    print("driver is insured:")
elif status=='unmarried' and age1>25 and gender=='female':
     print("driver is insured:")
else:
    print("driver not insured:")

#loops statements
#print natural numbers up to n

n=int(input("enter the number"))
i=1
while i<=n:
    print(i,end="")
    i=i+1
    
#print even and odd numbers up to n
no1=int(input("enter the number"))
i=1
while i<=no1:
    if i%2==0:
        print("even:",i)
    else:
        print("odd:",i)
        
        
#sum of natural numbers up to n
no2=int(input("enter the number"))
i=2
sum0=0
while i<=no2:
    sum0=sum0+i
    i=i+1
print("sum of natural numbers:",sum0)


#sum of even naturals numbers up to n
no3=int(input("enter the number"))
i=1
sum1=0
while i<=no3:
    if i%2==0:
        sum1=sum1+i
        i=i+1
print("sum of even numbers:",sum1)

#sum of odd naturals numbers up to n
no4=int(input("enter the number"))
i=1
sum2=0
while i<=no4:
    if i%2==1:
        sum2=sum2+i
        i=i+1
print("sum of even numbers:",sum2)


#print natural numbers in reverse up to n
n=int(input("enter the nuber"))
n=i
while n>=i:
    print(i,end="")
    i=i-1

#print fibnocci series
n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
print("\n")

#print number is prime or not
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")
print("\n")   

#print sum of digits entered by user
n=int(input("enter the nuber"))
sum=0
while num>0:
    num=n%10
    sum+=n
    n//=10
print(sum)
print("\n")

#check number is palindrome or not
n=int(input("enter the nuber"))

n=original
rev=0
while num>0:
    num=n%10
    rev=rev*10+n
    n//=10
if rev==original:
    print("palindrome")
else:
    print("not palindrome")
print("\n")

#print multipication table
n=int(int("enter the nuber"))
i=1
while n>=i:
    print(i*n,end="")
print("\n")

#print largest and smallest number from n numbers
n = int(input("Enter how many numbers: "))
num = int(input("Enter number: "))
largest = smallest = num
i = 2
while i <= n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    i += 1

print("Largest =", largest)
print("Smallest =", smallest)











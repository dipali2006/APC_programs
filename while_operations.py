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










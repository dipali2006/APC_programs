# number.py

def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def armstrong(n):
    s=0
    temp=n

    while temp>0:
        d=temp%10
        s=s+d**len(str(n))
        temp//=10

    return s==n

def palindrome(n):
    return str(n)==str(n)[::-1]

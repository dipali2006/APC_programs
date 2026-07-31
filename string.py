s1=input("enetr the string:")
count=0
for i in s1:
    count=count+1
print("lenght of string",count)


#count didgits numbers
s1=input("enter the string:")
count=0
count1=0
count2=0
count3=0
count4=0
for i in s1:
    if i in "aeiouAEIOU":
        count+=1
    else:
        count1+=1
print("vowels:",count)
print("consnants",count1)
for a in s1:
    if a==" ":
        count2+=1
print("white spaces:",count2)
for b in s1:
    if b.isdigit():
        count3+=1
print("digits count",count3)
for c in s1:
    if c in "@#$!&*?/^":
        count4+=1
print("symbol count:",count4)

#reverse the string
s1=input("enter the string:")
ch=""
for i in s1:
    ch=i+ch
print("reverse string",ch)

#check it is palindrome or not
s1=input("enter  the string")
if s1==s1[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")

#uppercase and lowercase count
s1=input("enter a string")
upper=0
lower=0
for i in s1:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print("upper count:",upper)
print("lower count:",lower)

#replace characters
s1="hello world"

print(s1.replace("o","m"))

#remove all spaces in string
s1=input("enter the string")
print(s1.strip())

#frequency of each character
s1=input("enter the string")
count={}
for ch in s1:
    count[ch]=count.get(ch,0)+1
for key,value in count.items():
    print(key,":",value)

#print first and last character in string
s1=input("enter the string")
print(s1[0])
print(s1[-1])

#Display each character of a string along with its ASCII value.
s1=input("enter the string")
for i in s1:
    print("ASCII values:",ord(i))


#Count the total number of words in a sentence
count=1
for i in s1:
    if i==" ":
        count+=1
print(count)

#longest word in string
text = "Python is a powerful programming language"

words = text.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

#shortest word in string
text = "Python is a powerful programming language"

words = text.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("shortest word:", shortest)

#use the title case
s1="python is a programming language"
print(s1.title())

#remove the duplicate characters

s1=input("enter the string")
dup=""
for ch in s1:
    if ch not in dup:
        dup+=ch
print(dup)


#check the string is anagram or not

s1=input("enter the first string")
s2=input("enter the second string")
if sorted(s1)==sorted(s2):
    print("the string is anagram")
else:
    print("the string is not angram")

print("\n\nString Programs")

# Run-Length Encoding
print("\n22. Run-Length Encoding")
s = input("Enter string: ")
count = 1
for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1


# String Compression
print("\n\n23. String Compression")
s = input("Enter string: ")
result = ""
count = 1
for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
if len(result) < len(s):
    print(result)
else:
    print(s)


# Most Frequent Character
print("\n24. Most Frequent Character")
s = input("Enter string: ")
max = 0
ch = ""
for i in s:
    if s.count(i) > max:
        max = s.count(i)
        ch = i
print(ch)


# Second Most Frequent Character
print("\n25. Second Most Frequent Character")
s = input("Enter string: ")
first = second = 0
fchar = schar = ""
for i in s:
    c = s.count(i)
    if c > first:
        second = first
        schar = fchar
        first = c
        fchar = i
    elif c > second and i != fchar:
        second = c
        schar = i
print(schar)


# Caesar Cipher (Encryption)
print("\n26. Caesar Cipher")
text = input("Enter text: ")
key = int(input("Enter key: "))
for ch in text:
    print(chr(ord(ch)+key), end="")


# Email Validator
print("\n\n27. Email Validator")
email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# Word Frequency
print("\n28. Word Frequency")
s = input("Enter sentence: ")
words = s.split()
for w in words:
    print(w, ":", words.count(w))


# Sentence Reversal
print("\n29. Sentence Reversal")
s = input("Enter sentence: ")
words = s.split()
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")


# String Rotation
print("\n\n30. String Rotation")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2) and s2 in (s1+s1):
    print("Yes")
else:
    print("No")



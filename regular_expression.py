# 1Write a Python program using regular expressions to extract all digits from a given string.

import re
s1 = "welcome to python programming123456789"
digits = re.findall(r"\d", s1)
print("Digits:", digits)


# 2Accept a sentence and display all words beginning with the letter A or a.

import re

sentence = input("Enter a sentence: ")

words = re.findall(r"\b[aA]\w*", sentence)

print("Words beginning with A or a:")
for word in words:
    print(word)

# 3Write a program to count the occurrences of vowels in a given string using regular expressions.

import re

text = input("Enter a string: ")

vowels = re.findall(r"[aeiouAEIOU]", text)

print("Total vowels:", len(vowels))
print("Vowels:", vowels)


# 4Write a program to extract all uppercase letters from a given string.

import re

text = input("Enter a string: ")

letters = re.findall(r"[A-Z]", text)

print("Uppercase letters:", letters)


# 5Write a program to identify all spaces, tabs, and newline characters in a text.

import re

text = "Python\tProgramming\nis fun"

characters = re.findall(r"\s", text)

print("Whitespace characters:", characters)
print("Count:", len(characters))

# 6 Write a program to replace multiple consecutive spaces with a single space.

import re

text = input("Enter a sentence: ")

result = re.sub(r"\s+", " ", text)

print("After replacement:")
print(result)

# 7 Accept a sentence and display all words containing exactly five characters.

import re

sentence = input("Enter a sentence: ")

words = re.findall(r"\b\w{5}\b", sentence)

print("Five-letter words:")
for word in words:
    print(word)


# 8 Write a program to identify all words ending with the letter s.

import re

sentence = input("Enter a sentence: ")

words = re.findall(r"\b\w*s\b", sentence)

print("Words ending with 's':")
for word in words:
    print(word)

# 9. Write a program to identify consecutive repeated words in a sentence, ignoring case differences.

import re

sentence = input("Enter a sentence: ")

repeated = re.findall(r'\b(\w+)\s+\1\b', sentence, re.IGNORECASE)

if repeated:
    print("Consecutive repeated words:")
    for word in repeated:
        print(word)
else:
    print("No consecutive repeated words found.")


# 10. Write a program to extract six-digit Indian PIN codes from a paragraph.

import re

text = input("Enter paragraph: ")

pins = re.findall(r"\b\d{6}\b", text)

print("PIN Codes:", pins)


# 11. Write a program to check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.

import re

vehicle = input("Enter vehicle number: ")

if re.fullmatch(r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}", vehicle):
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")



# 12. Write a program to extract file extensions from filenames in a given string.

import re

text = input("Enter filenames: ")

extensions = re.findall(r"\.\w+\b", text)

print("Extensions:", extensions)


# 13. Write a program to remove HTML tags, extra whitespace, and unwanted punctuation from a text document.

import re

text = input("Enter text: ")

text = re.sub(r"<.*?>", "", text)
text = re.sub(r"[^\w\s]", "", text)
text = re.sub(r"\s+", " ", text)

print(text.strip())


# 14. Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions.

import re

text = input("Enter invoice text: ")

invoice = re.findall(r"INV\d+", text)
dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
amounts = re.findall(r"\b\d+\.\d{2}\b", text)

print("Invoice Numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)


# 15. Write a program to identify single-line comments in Python source code.

import re

code = input("Enter Python code: ")

comments = re.findall(r"#.*", code)

print("Comments:", comments)

print("Regular expressions alone cannot correctly handle comments inside string literals or multiline strings.")



# 16. Validate product codes following the pattern ABC-1234-XY.

import re

code = input("Enter product code: ")

if re.fullmatch(r"[A-Z]{3}-\d{4}-[A-Z]{2}", code):
    print("Valid Product Code")
else:
    print("Invalid Product Code")

# 17. Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions.

import re

text = input("Enter student details: ")

records = re.findall(r"([A-Za-z]+)\s+(\d+)\s+(\d+)", text)

for name, roll, marks in records:
    print("Name:", name)
    print("Roll No:", roll)
    print("Marks:", marks)


# 18. Extract DOI identifiers, publication years, email addresses, and URLs from a collection of research paper references.

import re

text = input("Enter references: ")

doi = re.findall(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", text)
years = re.findall(r"\b(?:19|20)\d{2}\b", text)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
urls = re.findall(r"https?://\S+", text)

print("DOI:", doi)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)


# 19. Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.

import re

text = input("Enter a string: ")

result = re.sub(r"[^A-Za-z0-9 ]", "", text)

print("Result:", result)


# 20. Write a program to count the number of words in a sentence using regular expressions.

import re

sentence = input("Enter a sentence: ")

words = re.findall(r"\b\w+\b", sentence)

print("Number of words:", len(words))


# 21. Write a program to validate a 10-digit Indian mobile number using a regular expression.

import re

mobile = input("Enter mobile number: ")

if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# 22. Accept an email address and check whether it follows a reasonable email format.

import re

email = input("Enter email: ")

if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")


# 23. Write a program to extract dates in DD-MM-YYYY format from a given paragraph.

import re

text = input("Enter paragraph: ")

dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)

print("Dates:", dates)


# 24. Write a program to identify web addresses beginning with http:// or https://.

import re

text = input("Enter text: ")

urls = re.findall(r"https?://\S+", text)

print("URLs:", urls)


# 25. Write a program to extract all hashtags from a social media post.

import re

post = input("Enter post: ")

hashtags = re.findall(r"#\w+", post)

print("Hashtags:", hashtags)


# 26. Write a program to check whether a password contains at least eight characters, one uppercase letter, one lowercase letter, one digit, and one special character.

import re

password = input("Enter password: ")

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#]).{8,}$"

if re.fullmatch(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")




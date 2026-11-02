# Program 1
# Create a dictionary containing the following information for 5 students:
# Student ID, Student Name, Python Marks, DBMS Marks, Mathematics Marks.
# Convert the dictionary into a Pandas DataFrame and:
# 1. Display the DataFrame.
# 2. Calculate total marks for each student.
# 3. Calculate average marks.
# 4. Display students who scored more than 75% average.

import pandas as pd

data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Python Marks": [85, 70, 90, 65, 80],
    "DBMS Marks": [78, 88, 84, 72, 79],
    "Mathematics Marks": [92, 76, 81, 68, 75]
}

df = pd.DataFrame(data)

print("Student Data")
print(df)

df["Total"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average")
print(df)

print("\nStudents scoring more than 75% average")
print(df[df["Average"] > 75])


# Program 2
# Create a dictionary containing:
# Employee ID, Employee Name, Department, Salary, Experience.
# Convert it into a Pandas DataFrame and:
# 1. Display employees with salary greater than ₹50,000.
# 2. Find the average salary.
# 3. Find the highest salary.
# 4. Find the employee with the highest experience.

import pandas as pd

data = {
    "Employee ID": [1, 2, 3, 4, 5],
    "Employee Name": ["Amit", "Priya", "Rahul", "Neha", "Rohan"],
    "Department": ["IT", "HR", "IT", "Sales", "Finance"],
    "Salary": [60000, 45000, 70000, 55000, 48000],
    "Experience": [5, 2, 8, 4, 6]
}

df = pd.DataFrame(data)

print(df)

print("\nEmployees with Salary > 50000")
print(df[df["Salary"] > 50000])

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nHighest Salary")
print(df["Salary"].max())

print("\nEmployee with Highest Experience")
print(df.loc[df["Experience"].idxmax()])


# Program 3
# Create a dictionary containing:
# Product ID, Product Name, Category, Price, Quantity.
# Convert it into a DataFrame.
# Calculate Total Amount = Price × Quantity.
# Display the product having the highest total sales.

import pandas as pd

data = {
    "Product ID": [101, 102, 103, 104, 105],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Printer", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 500, 1500, 12000, 10000],
    "Quantity": [2, 20, 10, 3, 5]
}

df = pd.DataFrame(data)

df["Total Amount"] = df["Price"] * df["Quantity"]

print(df)

print("\nProduct with Highest Total Sales")
print(df.loc[df["Total Amount"].idxmax()])


# Program 4
# Create a dictionary containing:
# Patient ID, Patient Name, Age, Disease, Medical Charges.
# Convert the dictionary into a DataFrame and:
# 1. Display patients above 60 years.
# 2. Find the average medical charge.
# 3. Find the maximum medical charge.
# 4. Display patients whose medical charges are greater than ₹50,000.

import pandas as pd

data = {
    "Patient ID": [1, 2, 3, 4, 5],
    "Patient Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart", "Malaria", "BP"],
    "Medical Charges": [60000, 15000, 85000, 12000, 55000]
}

df = pd.DataFrame(data)

print(df)

print("\nPatients Above 60 Years")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge")
print(df["Medical Charges"].mean())

print("\nMaximum Medical Charge")
print(df["Medical Charges"].max())

print("\nPatients with Medical Charges > 50000")
print(df[df["Medical Charges"] > 50000])



# Program 5
# Create a dictionary containing:
# Order_ID, Customer, Product, Quantity, Price, Discount.
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount.
# Display:
# 1. All orders.
# 2. Orders above ₹5,000.
# 3. Highest-value order.
# 4. Average order value.

import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Product": ["Laptop", "Mouse", "Printer", "Keyboard", "Monitor"],
    "Quantity": [1, 5, 2, 4, 3],
    "Price": [50000, 500, 12000, 1500, 10000],
    "Discount": [2000, 100, 1000, 200, 500]
}

df = pd.DataFrame(data)

df["Final Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders")
print(df)

print("\nOrders Above ₹5000")
print(df[df["Final Amount"] > 5000])

print("\nHighest Value Order")
print(df.loc[df["Final Amount"].idxmax()])

print("\nAverage Order Value")
print(df["Final Amount"].mean())


# Program 6
# Create a dictionary containing:
# Student_ID, Name, Department, Total_Classes, Classes_Attended.
# Create a DataFrame and calculate:
# Attendance Percentage = (Classes_Attended / Total_Classes) × 100.
# Display students whose attendance is below 75%.

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "Mechanical"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [90, 68, 80, 72, 95]
}

df = pd.DataFrame(data)

df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Student Attendance")
print(df)

print("\nStudents with Attendance Below 75%")
print(df[df["Attendance Percentage"] < 75])

# Program 7
# A retail shop maintains sales information in a Python dictionary
# containing Product_ID, Product_Name, Category, Price, and Quantity.
# Write a Python program to:
# 1. Convert the dictionary into a Pandas DataFrame.
# 2. Add a new column Total_Sales.
# 3. Calculate Total_Sales = Price × Quantity.
# 4. Display products with sales greater than ₹10,000.
# 5. Find the product with maximum sales.
# 6. Calculate the average sales.

import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Printer", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 500, 1500, 12000, 10000],
    "Quantity": [2, 20, 10, 3, 5]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Retail Sales Data")
print(df)

print("\nProducts with Sales Greater than ₹10,000")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales")
print(df["Total_Sales"].mean())

# Program 8
# Create a Pandas Series using a dictionary where the student names
# are keys and their marks are values.
# Perform:
# 1. Display the Series.
# 2. Display marks of a particular student.
# 3. Find maximum and minimum marks.
# 4. Calculate the average marks.
# 5. Display students who scored more than 75.

import pandas as pd

marks = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 91,
    "Sneha": 68,
    "Rohan": 80
}

s = pd.Series(marks)

print("Student Marks")
print(s)

print("\nMarks of Rahul")
print(s["Rahul"])

print("\nMaximum Marks")
print(s.max())

print("\nMinimum Marks")
print(s.min())

print("\nAverage Marks")
print(s.mean())

print("\nStudents Scoring More Than 75")
print(s[s > 75])

# Program 9
# Create a Pandas Series using a dictionary containing employee
# names and their salaries.
# Perform:
# 1. Display the Series.
# 2. Find the highest salary.
# 3. Find the lowest salary.
# 4. Calculate average salary.
# 5. Display employees earning more than ₹50,000.

import pandas as pd

salary = {
    "Amit": 60000,
    "Priya": 45000,
    "Rahul": 70000,
    "Sneha": 55000,
    "Rohan": 48000
}

s = pd.Series(salary)

print("Employee Salaries")
print(s)

print("\nHighest Salary")
print(s.max())

print("\nLowest Salary")
print(s.min())

print("\nAverage Salary")
print(s.mean())

print("\nEmployees Earning More Than ₹50,000")
print(s[s > 50000])

# Program 10
# Create a Pandas Series using a dictionary containing product
# names and prices.
# Perform:
# 1. Display all products and prices.
# 2. Increase every price by 10%.
# 3. Find the most expensive product.
# 4. Find products costing more than ₹1,000.

import pandas as pd

price = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Printer": 12000,
    "Monitor": 10000
}

s = pd.Series(price)

print("Product Prices")
print(s)

print("\nPrices After 10% Increase")
print(s * 1.10)

print("\nMost Expensive Product")
print(s.idxmax(), "=", s.max())

print("\nProducts Costing More Than ₹1000")
print(s[s > 1000])

# Program 11
# Create a Pandas Series using a dictionary where student names are
# the keys and attendance percentages are the values.
# Perform:
# 1. Find the average attendance.
# 2. Display students with attendance below 75%.
# 3. Display students with attendance above 90%.
# 4. Find the highest attendance.

import pandas as pd

attendance = {
    "Amit": 92,
    "Priya": 70,
    "Rahul": 88,
    "Sneha": 95,
    "Rohan": 74
}

s = pd.Series(attendance)

print("Student Attendance")
print(s)

print("\nAverage Attendance")
print(s.mean())

print("\nStudents with Attendance Below 75%")
print(s[s < 75])

print("\nStudents with Attendance Above 90%")
print(s[s > 90])

print("\nHighest Attendance")
print(s.max())

# Program 12
# Dataset: students.csv
# Columns:
# Student_ID, Name, Department, Python, DBMS, Maths
#
# Read students.csv using Pandas and perform:
# 1. Display the first 5 records.
# 2. Display the last 5 records.
# 3. Find the total and average marks of each student.
# 4. Display students whose average marks are greater than 75.
# 5. Find the student with the highest average.
# 6. Find the average marks for each subject.

import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nStudent Total and Average")
print(df)

print("\nStudents with Average > 75")
print(df[df["Average"] > 75])

print("\nStudent with Highest Average")
print(df.loc[df["Average"].idxmax()])

print("\nAverage Marks of Each Subject")
print(df[["Python", "DBMS", "Maths"]].mean())


# Program 13
# Dataset: employees.csv
# Columns:
# Employee_ID, Name, Department, Experience, Salary
#
# Read employees.csv using Pandas and:
# 1. Display employees from the CSE department.
# 2. Find the average salary.
# 3. Find the highest and lowest salary.
# 4. Display employees having salary greater than ₹50,000.
# 5. Calculate department-wise average salary.

import pandas as pd

df = pd.read_csv("employees.csv")

print("Employees from CSE Department")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nHighest Salary")
print(df["Salary"].max())

print("\nLowest Salary")
print(df["Salary"].min())

print("\nEmployees with Salary > ₹50000")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary")
print(df.groupby("Department")["Salary"].mean())



# Program 14
# Dataset: patients.csv
# Columns:
# Patient_ID, Name, Age, Gender, Disease, Medical_Expense
#
# Read patients.csv using Pandas and:
# 1. Display patients above 60 years.
# 2. Calculate average medical expense.
# 3. Find the patient with the highest medical expense.
# 4. Count patients for each disease.
# 5. Display patients whose medical expense exceeds ₹50,000.

import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients Above 60 Years")
print(df[df["Age"] > 60])

print("\nAverage Medical Expense")
print(df["Medical_Expense"].mean())

print("\nPatient with Highest Medical Expense")
print(df.loc[df["Medical_Expense"].idxmax()])

print("\nDisease-wise Patient Count")
print(df["Disease"].value_counts())

print("\nPatients with Medical Expense > ₹50000")
print(df[df["Medical_Expense"] > 50000])


# Program 15
# Dataset: weather.csv
# Columns:
# Date, City, Temperature, Humidity, Rainfall
#
# Read weather.csv using Pandas and:
# 1. Find the maximum temperature.
# 2. Find the minimum temperature.
# 3. Calculate the average temperature.
# 4. Display records where temperature is above 35°C.
# 5. Calculate city-wise average temperature.

import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature")
print(df["Temperature"].max())

print("\nMinimum Temperature")
print(df["Temperature"].min())

print("\nAverage Temperature")
print(df["Temperature"].mean())

print("\nRecords with Temperature Above 35°C")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature")
print(df.groupby("City")["Temperature"].mean())



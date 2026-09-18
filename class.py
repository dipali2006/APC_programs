
# Create a class Student with attributes such as roll_no, name, and marks.
# Create objects for multiple students and display their details and percentage.

class Student:

    # Constructor
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    # Calculate percentage
    def calculate_percentage(self):
        return (self.marks / 500) * 100

    # Display student details
    def display(self):
        print("\nRoll No :", self.roll_no)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Percentage : {:.2f}%".format(self.calculate_percentage()))


# Input number of students
n = int(input("Enter number of students: "))

# Create student objects
students = []

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks (Out of 500): "))

    student = Student(roll_no, name, marks)
    students.append(student)

# Display student details
print("\nStudent Details")

for student in students:
    student.display()




# Create a class Employee with attributes emp_id, name, and basic_salary.
# Define methods to calculate HRA, DA, and gross salary.

class Employee:

    # Constructor
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    # Calculate HRA
    def calculate_hra(self):
        return self.basic_salary * 0.20

    # Calculate DA
    def calculate_da(self):
        return self.basic_salary * 0.10

    # Calculate Gross Salary
    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    # Display employee details
    def display(self):
        print("\nEmployee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA         :", self.calculate_hra())
        print("DA          :", self.calculate_da())
        print("Gross Salary:", self.calculate_gross_salary())


# Input employee details
emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Create object
employee = Employee(emp_id, name, basic_salary)

# Display details
employee.display()


# Create a class Rectangle with attributes length and breadth.
# Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

r = Rectangle(length, breadth)

print("Area:", r.area())
print("Perimeter:", r.perimeter())


# Create a class Circle with an attribute radius.
# Define methods to calculate the area and circumference of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


radius = float(input("Enter Radius: "))

c = Circle(radius)

print("Area:", c.area())
print("Circumference:", c.circumference())


# Create a class Book containing book_id, title, author, and price.
# Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("\nBook ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


books = []

for i in range(3):
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    price = float(input("Enter Price: "))
    books.append(Book(book_id, title, author, price))

for b in books:
    b.display()


# Create a class ElectricityBill containing consumer number, consumer name, and units consumed.
# Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 300:
            bill = 100 * 2 + (self.units - 100) * 3
        else:
            bill = 100 * 2 + 200 * 3 + (self.units - 300) * 5
        return bill

    def display(self):
        print("Consumer No:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Bill Amount:", self.calculate_bill())


consumer_no = int(input("Enter Consumer Number: "))
consumer_name = input("Enter Consumer Name: ")
units = int(input("Enter Units Consumed: "))

bill = ElectricityBill(consumer_no, consumer_name, units)
bill.display()

# Create a class MobilePhone with attributes brand, model, storage, and price.
# Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def discount_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)


brand = input("Enter Brand: ")
model = input("Enter Model: ")
storage = input("Enter Storage: ")
price = float(input("Enter Price: "))
discount = float(input("Enter Discount (%): "))

phone = MobilePhone(brand, model, storage, price)
phone.display()
print("Price After Discount:", phone.discount_price(discount))

# Create a class Patient containing patient ID, name, age, disease, and consultation fee.
# Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self):
        return self.consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Total Bill:", self.total_bill())


patient = Patient(
    int(input("Enter Patient ID: ")),
    input("Enter Name: "),
    int(input("Enter Age: ")),
    input("Enter Disease: "),
    float(input("Enter Consultation Fee: "))
)

patient.display()


# Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Create an object of the class and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account No:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


atm = ATM(
    int(input("Enter Account Number: ")),
    input("Enter Account Holder Name: "),
    float(input("Enter Balance: "))
)

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Display Account")
    print("5.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter Amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter Amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")

# Create a class Vehicle containing vehicle number, model, rental rate, and availability.
# Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self, days):
        if self.available:
            self.available = False
            print("Rental Charge:", days * self.rental_rate)
        else:
            print("Vehicle Not Available")

    def return_vehicle(self):
        self.available = True
        print("Vehicle Returned Successfully")

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.available)


vehicle = Vehicle(
    input("Enter Vehicle Number: "),
    input("Enter Model: "),
    float(input("Enter Rental Rate Per Day: "))
)

vehicle.display()

days = int(input("Enter Number of Days: "))
vehicle.rent(days)

vehicle.return_vehicle()
vehicle.display()


# Create a class ShoppingCart with customer name and cart ID.
# Initialize these values using a constructor.
# Implement methods to add products, remove products, and calculate the total bill.
# Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append((name, price))
        print("Product Added")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print("Product Removed")
                return
        print("Product Not Found")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        print("Total Bill:", total)

    def __del__(self):
        print("Shopping Cart Destroyed")


customer_name = input("Enter Customer Name: ")
cart_id = int(input("Enter Cart ID: "))

cart = ShoppingCart(customer_name, cart_id)

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Total Bill")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        cart.add_product(name, price)

    elif choice == 2:
        name = input("Enter Product Name: ")
        cart.remove_product(name)

    elif choice == 3:
        cart.total_bill()

    elif choice == 4:
        del cart
        break

    else:
        print("Invalid Choice")

# Create a class FoodOrder with order ID, customer name, food item, quantity, and price.
# Use a constructor to initialize the order.
# Define a method to calculate the total bill including tax.
# Implement a destructor to display an order completion message.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        print("Total Bill:", total + tax)

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)

    def __del__(self):
        print("Order Completed")


order = FoodOrder(
    int(input("Enter Order ID: ")),
    input("Enter Customer Name: "),
    input("Enter Food Item: "),
    int(input("Enter Quantity: ")),
    float(input("Enter Price: "))
)

order.display()
order.total_bill()

del order

# Create a class StudentResult with student name and marks in five subjects.
# Use a constructor to initialize the details.
# Define methods to calculate total, percentage, and grade.
# Implement a destructor to display a suitable message.

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        p = self.percentage()

        if p >= 75:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 50:
            return "C"
        elif p >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("Student Name:", self.name)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Result Generated Successfully")


name = input("Enter Student Name: ")

marks = []
for i in range(5):
    marks.append(float(input("Enter Marks of Subject {}: ".format(i + 1))))

student = StudentResult(name, marks)

student.display()

del student






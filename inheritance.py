

# Create a class Employee with attributes emp_id, name, and salary.
# Create a derived class Manager that inherits from Employee and contains an additional attribute department.
# Display all employee and manager details and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
salary = float(input("Enter Salary: "))
department = input("Enter Department: ")

m = Manager(emp_id, name, salary, department)
m.display()

# Create a base class Vehicle with attributes brand and model.
# Create a derived class Car with additional attributes fuel_type and price.
# Define methods to display vehicle details and calculate the discounted price of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discount(self, percent):
        print("Discounted Price:", self.price - (self.price * percent / 100))

brand = input("Enter Brand: ")
model = input("Enter Model: ")
fuel = input("Enter Fuel Type: ")
price = float(input("Enter Price: "))
d = float(input("Enter Discount (%): "))

c = Car(brand, model, fuel, price)
c.display()
c.discount(d)

# Create two classes Academic and Sports.
# The Academic class should store marks obtained by a student, while the Sports class should store sports points.
# Create a class Student that inherits from both classes and calculates the student's overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, points):
        self.points = points

class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def display(self):
        total = self.marks + self.points
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", total)

marks = int(input("Enter Academic Marks: "))
points = int(input("Enter Sports Points: "))

s = Student(marks, points)
s.display()


# Create classes PersonalDetails and ProfessionalDetails.
# Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class.
# Create an Employee class that inherits from both classes and displays complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
emp_id = int(input("Enter Employee ID: "))
designation = input("Enter Designation: ")
salary = float(input("Enter Salary: "))

e = Employee(name, age, emp_id, designation, salary)
e.display()

# Create a class Person containing name and age.
# Derive a class Student from Person with roll number and course.
# Further derive a class ResearchStudent from Student with research topic and guide name.
# Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
roll_no = int(input("Enter Roll No: "))
course = input("Enter Course: ")
topic = input("Enter Research Topic: ")
guide = input("Enter Guide Name: ")

r = ResearchStudent(name, age, roll_no, course, topic, guide)
r.display()

# Create a base class BankAccount with account number and balance.
# Derive SavingsAccount from it with an interest rate.
# Further derive PremiumSavingsAccount with additional benefits.
# Define methods to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        interest = self.balance * self.interest_rate / 100
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)
        print("Interest:", interest)
        print("Benefits:", self.benefits)

account_no = int(input("Enter Account Number: "))
balance = float(input("Enter Balance: "))
interest_rate = float(input("Enter Interest Rate: "))
benefits = input("Enter Benefits: ")

p = PremiumSavingsAccount(account_no, balance, interest_rate, benefits)
p.display()


# Create a base class Shape containing a method to display the name of the shape.
# Create three derived classes Circle, Rectangle, and Triangle.
# Each class should implement its own method to calculate the area.

class Shape:
    def display_name(self):
        print("Shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area:", self.length * self.breadth)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Area:", 0.5 * self.base * self.height)

c = Circle(float(input("Enter Radius: ")))
c.display_name()
c.area()

r = Rectangle(float(input("Enter Length: ")), float(input("Enter Breadth: ")))
r.display_name()
r.area()

t = Triangle(float(input("Enter Base: ")), float(input("Enter Height: ")))
t.display_name()
t.area()

# Create a base class Employee containing employee ID, name, and basic salary.
# Create derived classes Manager, Developer, and Tester.
# Each derived class should calculate salary differently based on its respective allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

class Manager(Employee):
    def salary(self):
        print("Manager Salary:", self.basic_salary + 10000)

class Developer(Employee):
    def salary(self):
        print("Developer Salary:", self.basic_salary + 7000)

class Tester(Employee):
    def salary(self):
        print("Tester Salary:", self.basic_salary + 5000)

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
basic_salary = float(input("Enter Basic Salary: "))

m = Manager(emp_id, name, basic_salary)
d = Developer(emp_id, name, basic_salary)
t = Tester(emp_id, name, basic_salary)

m.salary()
d.salary()
t.salary()

# Create a class Person.
# Derive Student and Faculty from Person.
# Create another class TeachingAssistant that inherits from both Student and Faculty.
# Display the details and demonstrate the use of multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

class Faculty(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll_no, subject):
        Student.__init__(self, name, roll_no)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)

name = input("Enter Name: ")
roll_no = int(input("Enter Roll No: "))
subject = input("Enter Subject: ")

ta = TeachingAssistant(name, roll_no, subject)
ta.display()



# Create a base class Vehicle.
# Derive Car and Bike from Vehicle.
# Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike.
# Add suitable attributes and methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Top Speed:", self.top_speed)

class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery)

sc = SportsCar(
    input("Enter Car Brand: "),
    input("Enter Car Model: "),
    input("Enter Top Speed: ")
)

eb = ElectricBike(
    input("Enter Bike Brand: "),
    input("Enter Bike Model: "),
    input("Enter Battery Capacity: ")
)

sc.display()
eb.display()

# Create a base class Student with attributes roll_no, name, and course.
# Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)

r = Result(
    int(input("Enter Roll No: ")),
    input("Enter Name: "),
    input("Enter Course: "),
    float(input("Enter Marks 1: ")),
    float(input("Enter Marks 2: ")),
    float(input("Enter Marks 3: "))
)

r.display()

# Create a class Product with product ID, name, and price.
# Derive ElectronicProduct with additional attributes such as brand and warranty.
# Calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def display(self, discount):
        final_price = self.price - (self.price * discount / 100)
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Original Price:", self.price)
        print("Final Price:", final_price)

ep = ElectronicProduct(
    int(input("Enter Product ID: ")),
    input("Enter Product Name: "),
    float(input("Enter Price: ")),
    input("Enter Brand: "),
    input("Enter Warranty: ")
)

discount = float(input("Enter Discount (%): "))
ep.display(discount)


# Create classes Printer and Scanner with suitable methods for printing and scanning documents.
# Create a MultifunctionDevice class that inherits from both and supports both operations.

class Printer:
    def print_document(self):
        print("Printing Document")

class Scanner:
    def scan_document(self):
        print("Scanning Document")

class MultifunctionDevice(Printer, Scanner):
    pass

m = MultifunctionDevice()
m.print_document()
m.scan_document()

# Create classes Camera and Phone.
# The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls.
# Create a Smartphone class inheriting from both.

class Camera:
    def take_photo(self):
        print("Photo Captured")

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()
s.take_photo()
s.make_call()

# Create a class Person with name and age.
# Derive Student with roll number and course.
# Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)

r = ResearchStudent(
    input("Enter Name: "),
    int(input("Enter Age: ")),
    int(input("Enter Roll No: ")),
    input("Enter Course: "),
    input("Enter Research Topic: "),
    input("Enter Guide Name: ")
)

r.display()

# Create a class Person with name and age.
# Derive Student with roll number and course.
# Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)

r = ResearchStudent(
    input("Enter Name: "),
    int(input("Enter Age: ")),
    int(input("Enter Roll No: ")),
    input("Enter Course: "),
    input("Enter Research Topic: "),
    input("Enter Guide Name: ")
)

r.display()

# Create a base class Animal with common attributes and methods.
# Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")

class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow")

class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo")

dog = Dog(input("Enter Dog Name: "))
cat = Cat(input("Enter Cat Name: "))
cow = Cow(input("Enter Cow Name: "))

dog.sound()
cat.sound()
cow.sound()

# Create a class Person and derive Doctor and Patient.
# Create additional classes representing Surgeon and MedicalResearcher.
# Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization

class Patient(Person):
    def __init__(self, name, disease):
        super().__init__(name)
        self.disease = disease

class Surgeon(Doctor):
    def display(self):
        print("Surgeon:", self.name)
        print("Specialization:", self.specialization)

class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, specialization, disease):
        Doctor.__init__(self, name, specialization)
        self.disease = disease

    def display(self):
        print("Researcher:", self.name)
        print("Specialization:", self.specialization)
        print("Research Disease:", self.disease)

s = Surgeon(
    input("Enter Surgeon Name: "),
    input("Enter Specialization: ")
)

m = MedicalResearcher(
    input("Enter Researcher Name: "),
    input("Enter Specialization: "),
    input("Enter Research Disease: ")
)

s.display()
m.display()










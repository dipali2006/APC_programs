# Create a base class Shape with a method area(). Derive Circle, Rectangle,
# and Triangle classes and override the area() method in each class.
# Create objects of each class and demonstrate runtime polymorphism.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle =", self.l * self.b)

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print("Area of Triangle =", 0.5 * self.b * self.h)

shapes = [Circle(5), Rectangle(10, 4), Triangle(6, 8)]

for shape in shapes:
    shape.area()


# Create a base class Employee with a method calculate_salary().
# Derive Manager, Developer, and Tester classes.
# Override the method in each class to calculate salary according to the employee's role.

class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary = 70000")

class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary = 50000")

class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary = 35000")

employees = [Manager(), Developer(), Tester()]

for employee in employees:
    employee.calculate_salary()


# Create a base class Vehicle with a method start().
# Derive Car, Bike, and Bus classes and override start()
# to display the starting behavior of each vehicle.

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start.")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with engine ignition.")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()

# Create a base class Animal with a method sound().
# Create subclasses Dog, Cat, Cow, and Lion.
# Override sound() in each class to display the appropriate sound.

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog : Bark")

class Cat(Animal):
    def sound(self):
        print("Cat : Meow")

class Cow(Animal):
    def sound(self):
        print("Cow : Moo")

class Lion(Animal):
    def sound(self):
        print("Lion : Roar")

animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# Create a base class Notification with a method send().
# Derive EmailNotification, SMSNotification, and PushNotification.
# Override send() to display the appropriate notification method.

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Notification sent through Email.")

class SMSNotification(Notification):
    def send(self):
        print("Notification sent through SMS.")

class PushNotification(Notification):
    def send(self):
        print("Notification sent through Push Notification.")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# Create a base class Student with a method calculate_grade().
# Derive EngineeringStudent, MedicalStudent, and ManagementStudent.
# Override the method according to different grading criteria.

class Student:
    def calculate_grade(self):
        pass

class EngineeringStudent(Student):
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            print("Engineering Student Grade = A")
        elif self.marks >= 60:
            print("Engineering Student Grade = B")
        else:
            print("Engineering Student Grade = C")

class MedicalStudent(Student):
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 85:
            print("Medical Student Grade = A")
        elif self.marks >= 70:
            print("Medical Student Grade = B")
        else:
            print("Medical Student Grade = C")

class ManagementStudent(Student):
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 75:
            print("Management Student Grade = A")
        elif self.marks >= 60:
            print("Management Student Grade = B")
        else:
            print("Management Student Grade = C")

students = [
    EngineeringStudent(82),
    MedicalStudent(88),
    ManagementStudent(72)
]

for student in students:
    student.calculate_grade()


# Create a base class BankAccount with a method calculate_interest().
# Derive SavingsAccount, CurrentAccount, and FixedDepositAccount.
# Override the method to calculate interest differently for each account type.

class BankAccount:
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, amount):
        self.amount = amount

    def calculate_interest(self):
        interest = self.amount * 0.04
        print("Savings Account Interest =", interest)

class CurrentAccount(BankAccount):
    def __init__(self, amount):
        self.amount = amount

    def calculate_interest(self):
        print("Current Account Interest = 0")

class FixedDepositAccount(BankAccount):
    def __init__(self, amount):
        self.amount = amount

    def calculate_interest(self):
        interest = self.amount * 0.07
        print("Fixed Deposit Interest =", interest)

accounts = [
    SavingsAccount(10000),
    CurrentAccount(10000),
    FixedDepositAccount(10000)
]

for account in accounts:
    account.calculate_interest()


# Create a base class Report with a method generate().
# Derive PDFReport, ExcelReport, and HTMLReport.
# Write a function that accepts any report object and calls generate().

class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")

def create_report(report):
    report.generate()

create_report(PDFReport())
create_report(ExcelReport())
create_report(HTMLReport())


# Create a class Distance with feet and inches.
# Overload the + operator to add two distance objects
# and display the result in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        if inches >= 12:
            feet += inches // 12
            inches = inches % 12

        return Distance(feet, inches)

    def display(self):
        print("Distance =", self.feet, "feet", self.inches, "inches")

d1 = Distance(5, 8)
d2 = Distance(4, 9)

d3 = d1 + d2
d3.display()


# Create a class Student containing the student's name and total marks.
# Overload the > and < operators to compare the marks of two students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Rahul", 85)
s2 = Student("Priya", 78)

if s1 > s2:
    print(s1.name, "has higher marks.")
else:
    print(s2.name, "has higher marks.")

if s1 < s2:
    print(s1.name, "has lower marks.")
else:
    print(s2.name, "has lower marks.")



# Create a class Product with product name and price.
# Overload the == and > operators to compare two products based on their prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 30000)

if p1 == p2:
    print("Both products have the same price.")
else:
    print("Products have different prices.")

if p1 > p2:
    print(p1.name, "is more expensive than", p2.name)
else:
    print(p2.name, "is more expensive than", p1.name)


# Develop an online shopping payment module using polymorphism.
# Create a base class Payment and derived classes UPIPayment,
# CardPayment, and WalletPayment.
# Each class should implement its own make_payment() method.
# Demonstrate polymorphism using a common function.

class Payment:
    def make_payment(self):
        pass

class UPIPayment(Payment):
    def make_payment(self):
        print("Payment made using UPI.")

class CardPayment(Payment):
    def make_payment(self):
        print("Payment made using Card.")

class WalletPayment(Payment):
    def make_payment(self):
        print("Payment made using Wallet.")

def process_payment(payment):
    payment.make_payment()

process_payment(UPIPayment())
process_payment(CardPayment())
process_payment(WalletPayment())


# Create a base class Person with a method display_role().
# Derive Student, Faculty, and Administrator.
# Override the method to display the respective role.
# Store all objects in a list and invoke the same method using a loop.

class Person:
    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print("Role : Student")

class Faculty(Person):
    def display_role(self):
        print("Role : Faculty")

class Administrator(Person):
    def display_role(self):
        print("Role : Administrator")

persons = [Student(), Faculty(), Administrator()]

for person in persons:
    person.display_role()


# Create a base class Media with a method play().
# Derive Audio, Video, and Podcast.
# Override play() according to the media type.

class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing Audio.")

class Video(Media):
    def play(self):
        print("Playing Video.")

class Podcast(Media):
    def play(self):
        print("Playing Podcast.")

media_list = [Audio(), Video(), Podcast()]

for media in media_list:
    media.play()


# Create a base class SmartDevice with methods turn_on() and turn_off().
# Derive Light, Fan, AC, and TV.
# Override the methods according to each device.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")

class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")

class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

devices = [Light(), Fan(), AC(), TV]

for device in devices:
    device.turn_on()
    device.turn_off()


# Create an abstract class Shape with an abstract method area().
# Derive Circle, Rectangle, and Triangle classes and implement
# the area() method for each shape.
# Create objects of the derived classes and display their areas.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle =", self.l * self.b)

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print("Area of Triangle =", 0.5 * self.b * self.h)

c = Circle(5)
r = Rectangle(10, 4)
t = Triangle(6, 8)

c.area()
r.area()
t.area()



# Create an abstract class Vehicle with abstract methods
# start() and stop(). Derive Car, Bike, and Bus classes
# and implement these methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")

class Bus(Vehicle):

    def start(self):
        print("Bus Started")

    def stop(self):
        print("Bus Stopped")

vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()
    v.stop()


# Create an abstract class BankAccount with abstract methods
# deposit() and withdraw(). Derive SavingsAccount and
# CurrentAccount and implement the required operations.

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):

    def __init__(self):
        self.balance = 10000

    def deposit(self, amount):
        self.balance += amount
        print("Savings Balance =", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Savings Balance =", self.balance)

class CurrentAccount(BankAccount):

    def __init__(self):
        self.balance = 15000

    def deposit(self, amount):
        self.balance += amount
        print("Current Balance =", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Current Balance =", self.balance)

s = SavingsAccount()
s.deposit(2000)
s.withdraw(1000)

c = CurrentAccount()
c.deposit(3000)
c.withdraw(1500)


# Create an abstract class FoodOrder with abstract methods
# calculate_bill() and delivery_charge().
# Derive RestaurantOrder and HomeDeliveryOrder and
# implement the methods appropriately.

from abc import ABC, abstractmethod

class FoodOrder(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):

    def calculate_bill(self):
        print("Restaurant Bill = 500")

    def delivery_charge(self):
        print("Delivery Charge = 0")

class HomeDeliveryOrder(FoodOrder):

    def calculate_bill(self):
        print("Food Bill = 500")

    def delivery_charge(self):
        print("Delivery Charge = 50")

r = RestaurantOrder()
r.calculate_bill()
r.delivery_charge()

h = HomeDeliveryOrder()
h.calculate_bill()
h.delivery_charge()


# Create an abstract class Patient with abstract methods
# calculate_bill() and treatment().
# Derive InPatient, OutPatient, and EmergencyPatient.
# Implement the methods according to the patient type.

from abc import ABC, abstractmethod

class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):

    def calculate_bill(self):
        print("InPatient Bill = 10000")

    def treatment(self):
        print("Room Admission Treatment")

class OutPatient(Patient):

    def calculate_bill(self):
        print("OutPatient Bill = 500")

    def treatment(self):
        print("Regular Checkup")

class EmergencyPatient(Patient):

    def calculate_bill(self):
        print("Emergency Bill = 15000")

    def treatment(self):
        print("Emergency Treatment")

patients = [InPatient(), OutPatient(), EmergencyPatient()]

for p in patients:
    p.calculate_bill()
    p.treatment()


# Create an abstract class Transport with an abstract method
# calculate_fare(distance). Implement subclasses:
# Bus, Train, Taxi, and Flight.
# Calculate the fare according to the transportation type.

from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):

    def calculate_fare(self, distance):
        print("Bus Fare =", distance * 5)

class Train(Transport):

    def calculate_fare(self, distance):
        print("Train Fare =", distance * 3)

class Taxi(Transport):

    def calculate_fare(self, distance):
        print("Taxi Fare =", distance * 15)

class Flight(Transport):

    def calculate_fare(self, distance):
        print("Flight Fare =", distance * 50)

distance = 100

vehicles = [Bus(), Train(), Taxi(), Flight()]

for vehicle in vehicles:
    vehicle.calculate_fare(distance)


# Create an abstract class Question with an abstract method
# evaluate_answer().
# Derive:
# MCQQuestion
# TrueFalseQuestion
# DescriptiveQuestion
# Implement answer evaluation for each question type.

from abc import ABC, abstractmethod

class Question(ABC):

    @abstractmethod
    def evaluate_answer(self):
        pass

class MCQQuestion(Question):

    def evaluate_answer(self):
        print("MCQ Answer is Correct")

class TrueFalseQuestion(Question):

    def evaluate_answer(self):
        print("True/False Answer is Correct")

class DescriptiveQuestion(Question):

    def evaluate_answer(self):
        print("Descriptive Answer Evaluated")

questions = [
    MCQQuestion(),
    TrueFalseQuestion(),
    DescriptiveQuestion()
]

for question in questions:
    question.evaluate_answer()


# Create an abstract class Authentication with an abstract
# method authenticate().
# Implement the method using:
# Password authentication
# OTP authentication
# Biometric authentication.
# Demonstrate abstraction by interacting with objects
# through the abstract interface.

from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):

    def authenticate(self):
        print("Authenticated using Password")

class OTPAuthentication(Authentication):

    def authenticate(self):
        print("Authenticated using OTP")

class BiometricAuthentication(Authentication):

    def authenticate(self):
        print("Authenticated using Fingerprint")

methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.authenticate()


# Create an abstract class CloudStorage with abstract methods:
# upload_file()
# download_file()
# delete_file()
# Create subclasses representing different storage services
# and implement the operations.

from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class GoogleDrive(CloudStorage):

    def upload_file(self):
        print("File Uploaded to Google Drive")

    def download_file(self):
        print("File Downloaded from Google Drive")

    def delete_file(self):
        print("File Deleted from Google Drive")

class Dropbox(CloudStorage):

    def upload_file(self):
        print("File Uploaded to Dropbox")

    def download_file(self):
        print("File Downloaded from Dropbox")

    def delete_file(self):
        print("File Deleted from Dropbox")

class OneDrive(CloudStorage):

    def upload_file(self):
        print("File Uploaded to OneDrive")

    def download_file(self):
        print("File Downloaded from OneDrive")

    def delete_file(self):
        print("File Deleted from OneDrive")

storage = [
    GoogleDrive(),
    Dropbox(),
    OneDrive()
]

for s in storage:
    s.upload_file()
    s.download_file()
    s.delete_file()


# Create an abstract class Appointment with abstract methods
# book_appointment() and calculate_fee().
# Derive GeneralAppointment, SpecialistAppointment,
# and EmergencyAppointment.

from abc import ABC, abstractmethod

class Appointment(ABC):

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):

    def book_appointment(self):
        print("General Appointment Booked")

    def calculate_fee(self):
        print("Consultation Fee = 500")

class SpecialistAppointment(Appointment):

    def book_appointment(self):
        print("Specialist Appointment Booked")

    def calculate_fee(self):
        print("Consultation Fee = 1000")

class EmergencyAppointment(Appointment):

    def book_appointment(self):
        print("Emergency Appointment Booked")

    def calculate_fee(self):
        print("Consultation Fee = 2000")

appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    appointment.calculate_fee()



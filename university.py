# Exercise 7 - Object-Oriented Programming

# d) Bonus task
# As both students and professors have a first name, last name and age, you think of a cleaner solution:
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Create a Person class, which is the parent class of Student and Professor classes
# This Person class has the following properties: "first_name", "last_name" and "age"
# and following method: "print_name", which can print the full name
# So you don't need the properties and the method in the other two classes. You can easily inherit these.
# Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(f"{self.first_name} {self.last_name}")

# a) Create a Student class
# with properties:
# first name
# last name
# age
# lectures they attend
# with methods:
# can print the full name
# can list the lectures, which the student attends
# can add new lectures to the lectures list (attend a new lecture)
# can remove lectures from the lectures list (leave a lecture)
class Student(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def list_lectures(self):
        for lecture in self.lectures:
            lecture.name_duration()

    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def remove_lecture(self, lecture):
        self.lectures.remove(lecture)

# b) Create a Professor class
# with properties:
# first name
# last name
# age
# subjects they teach
# with methods:
# can print the full name
# can list the subjects they teach
# can add new subjects to the list
# can remove subjects from the list
class Professor(Person):
    def __init__(self, first_name, last_name, age, subjects):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects

    def list_subjects(self):
        print(f"{self.subjects}")

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

# c) Create a Lecture class
# with properties:
# name
# max number of students
# duration
# list of professors giving this lecture
# with methods:
# printing the name and duration of the lecture
# adding professors to the list of professors giving this lecture
class Lecture():
    def __init__(self, name, max_num_of_students, duration, professors):
        self.name = name
        self.max_num_of_students = max_num_of_students
        self.duration = duration
        self.professors = professors

    def name_duration(self):
        print(f"{self.name} {self.duration}")

    def add_professor(self, professors):
        self.professors += professors
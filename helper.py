# Exercise 4 - Helper Functions

# Write a function that accepts a list of dictionaries with employee age (see example list from Exercise 3) and prints out the name and age of the youngest employee.
def youngest_employee(employees):
    youngest = employees[0]
    for i in range (1, len(employees)):
        if employees[i]["age"] < youngest["age"]:
            youngest = employees[i]
    print(f"The youngest employee is {youngest["name"]}, who is {youngest["age"]} years old")

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
def num_of_upper_lower_case_letters(text):
    upper_case_letters = []
    lower_case_letters = []
    for letter in text:
        if letter.isupper():
            upper_case_letters.append(letter)
        elif letter.islower():
            lower_case_letters.append(letter)
    print(f"The number of uppercase letters is {len(upper_case_letters)}, the number of lowercase letters is {len(lower_case_letters)}")

# Write a function that prints the even numbers from a provided list.
def even_numbers(numbers):
    evens_only = []
    for number in numbers:
        if number % 2 == 0:
            evens_only.append(number)
    print(f"The even numbers are {evens_only}")

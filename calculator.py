# Exercise 5 - Calculator

# Write a simple calculator program that:
# takes user input of 2 numbers and operation to execute
# handles the following operations: plus, minus, multiply, divide
# does proper user validation and give feedback: only numbers allowed
# Keeps the Calculator program running until the user types “exit”
# Keeps track of how many calculations the user has taken, and when the user exits the calculator program, 
# prints out the number of calculations the user did
def calculator():
    allowed_operators = ["+", "-", "*", "/"]
    num_of_calculations = 0

    while True:
        user_input = input(f"Calculator, Supported operators are {allowed_operators} \nEnter <num1> <ops> <num2> space separated: \n")
        if user_input == "exit":
            print(f"Total of {num_of_calculations} calculations completed, Goodbye!")
            return 0

        if len(user_input.split()) != 3:
            print(f"Invalid input format {user_input}")
            continue

        [num1, op, num2] = user_input.split()

        if op not in allowed_operators:
            print(f"Invalid operator {op}")
            continue
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print(f"Invalid numbers {num1} {num2}")
            continue

        if op == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")

        num_of_calculations += 1
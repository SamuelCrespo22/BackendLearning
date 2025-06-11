"""
This module implements a simple calculator using only functions.
"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0:
        raise ValueError("You can't divide by zero.")
    return a / b

def get_number(prompt):
    while True: # keep asking number until it is valid. Once it returns, gets out of the loop.
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")

def choose_operation():
    operations = {
        "1" : ("Add", add),
        "2" : ("Subtract", subtract),
        "3" : ("Multiply", multiply),
        "4" : ("Divide", divide) 
    }
    while True:
        print("\nChoose an operation:")
        for key, (name, _) in operations.items(): #items returns the tuple (key, value), but here value is a tuple (str, function).
            print(f"  {key}) {name}")

        choice = input()
        if choice in operations: # checks if choice is 1, 2, 3 or 4.
            return operations[choice][1] # returns only the index 1 inside the value of the choice (key), which is a function.
        
        print("Invalid choice, try again.")

def next_thing(answer):
    while True:
        print(f"\nAnswer: {answer}")
        print("What do you want to do now?")
        print("1) Use answer for another operation.")
        print("2) Restart with new numbers.")
        print("3) Exit.")
        choice = input()
        if choice == "1":
            return True, answer, get_number("Second number:")
        if choice == "2":
            return True, get_number("First number:"), get_number("Second number:")
        if choice == "3":
            return False, None, None

def main():
    num1 = get_number("First number:")
    num2 = get_number("Second number:")
    continue_operations = True

    while continue_operations:
        operation = choose_operation()
        try:
            answer = operation(num1, num2)
        except Exception as e:
            print(f"Error: {e}")
            continue

        continue_operations, num1, num2 = next_thing(answer)


if __name__ == '__main__':
    main()
# ----------------------------
# Task 1: Perform Basic Mathematical Operations
# ----------------------------

# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying results
print("\n--- Results ---")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# ----------------------------
# Task 2: Create a Personalized Greeting
# ----------------------------

# Taking name input
first_name = input("\nEnter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating full name
full_name = first_name + " " + last_name

# Greeting message
print(f"\nHello, {full_name} Welcome to tute python.")

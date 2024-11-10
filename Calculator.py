# Calculator script in Python

# Function to add two numbers
def add(x, y):
    # Returns the sum of x and y
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    # Returns the difference between x and y
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    # Returns the product of x and y
    return x * y


# Function to divide two numbers (with a check to prevent division by zero)
def divide(x, y):
    # Checks if the denominator is not zero to avoid division by zero error
    if y != 0:
        return x / y
    else:
        # Returns an error message if the denominator is zero
        return "Error! Division by zero."


# Display the options to the user
print("Select operation:")
print("1. Add")  # Option for addition
print("2. Subtract")  # Option for subtraction
print("3. Multiply")  # Option for multiplication
print("4. Divide")  # Option for division

# Get user input for operation selection
choice = input("Enter choice (1/2/3/4): ")  # Prompts user to choose an operation

# Check if the chosen operation is valid
if choice in ('1', '2', '3', '4'):
    try:
        # Get input for the two numbers
        num1 = float(input("Enter first number: "))  # Prompts user to enter the first number and converts it to float
        num2 = float(input("Enter second number: "))  # Prompts user to enter the second number and converts it to float

        # Perform the chosen operation and display the result
        if choice == '1':
            # Calls the add function and prints the result
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            # Calls the subtract function and prints the result
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            # Calls the multiply function and prints the result
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            # Calls the divide function and prints the result
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input! Please enter numeric values.")
else:
    # Handle the case where the operation choice is invalid
    print("Invalid choice! Please select a valid operation.")
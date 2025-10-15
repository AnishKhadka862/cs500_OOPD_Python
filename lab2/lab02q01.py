#lab 02 question 01
print("a simple calculator\n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, or /): ")

# Check the operation and perform the calculation accordingly
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    # error handling if division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
#print error if invalid operation entered
else:
    print("Error: Invalid operation. Please use +, -, *, or /")
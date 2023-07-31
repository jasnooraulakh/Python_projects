print("Hello, welcome to simple calculator!")

# Prompt user to input 2 numbers
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
result = 0

# Inquire user about the operation to be performed
operation = input("Please enter the operator (+, -, *, /, //, **, %): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '//':
    result = num1 // num2
elif operation == '**':
    result = num1 ** num2
elif operation == '%':
    result = num1 % num2

# Print the result
print(result)
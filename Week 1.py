# Calculator

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))
operation = input("Operation (+)(-)(*)(/): ")
result: int

if operation == '+':
    result = firstNumber + secondNumber
elif operation == '-':
    result = firstNumber - secondNumber
elif operation == '*':
    result = firstNumber * secondNumber
elif operation == '/':
    result = firstNumber / secondNumber

print(result)

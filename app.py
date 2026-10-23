number1 = float(input("Enter the first number: "))
operator = input("Enter the operator for the desired operation(+,-,*,/): ")
number2 = float(input("Enter the second number: "))

if operator == "+": 
    result = number1 + number2
    print(result)
elif operator == "-": 
    result = number1 - number2
    print(result)
elif operator == "*": 
    result = number1 * number2
    print(result) 
elif operator == "/": 
    print(result)
else: 
    print("This operation is not recognised by me")

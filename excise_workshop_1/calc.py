def add(number1,number2):
    return number1 + number2
def subtract(number1,number2):
    return number1 - number2
def divide(number1,number2):
    return number1 / number2
def multi(number1,number2):
    return number1 * number2
def run():
    operator = input("enter operator ")
    number1 = int(input("Enter number1 "))
    number2 = int(input("Enter number2 "))

    if operator == "+":
        print(add(number1,number2))
    elif operator == "-":
        print(subtract(number1,number2))
    elif operator == "-":
        print(divide(number1,number2))
    elif operator == "-":
        print(multi(number1,number2))
    else:
        print("not valid operator")
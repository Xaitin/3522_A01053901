import math


def calculate_hypotenuse(a, b):
    return math.sqrt((a*a)+(b*b))


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def main():
    print("1 to calculate hypotenuse")
    print("2 to add")
    print("3 to subtract")
    print("4 to multiply")
    print("5 to divide")
    des_op = int(input())
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if des_op == 1:
        print(calculate_hypotenuse(num1, num2))
    elif des_op == 2:
        print(add(num1, num2))
    elif des_op == 3:
        print(subtract(num1, num2))
    elif des_op == 4:
        print(multiply(num1, num2))
    elif des_op == 5:
        print(divide(num1, num2))
    else:
        print("Invalid Entry")
        main()


if __name__ == '__main__':
    main()

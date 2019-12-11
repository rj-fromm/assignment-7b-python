#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Dec 2019
# This program uses an array


def subtract(x, y):
    return x - y


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def main():

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1, num2))
        print(num1, "-", num2, "=", subtract(num1, num2))
        print(num1, "*", num2, "=", multiply(num1, num2))

    except Exception:
        print("Invalid number")


if __name__ == "__main__":
    main()

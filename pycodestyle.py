#!/usr/bin/python3

def factorial(n):
    """
    Calculate the factorial of a positive integer.
    Args:
        n (int): The input integer.
    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    try:
        num = int(input("Enter a positive integer: "))
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()


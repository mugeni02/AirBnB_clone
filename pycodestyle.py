import sys

def greet(name):
    """
    Greets a person by name.

    :param name: The name of the person to greet.
    :type name: str
    :return: A greeting message.
    :rtype: str
    """
    return f"Hello, {name}! Welcome to our world of beautiful code."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python beautiful_code.py <your_name>")
        sys.exit(1)

    name = sys.argv[1]
    message = greet(name)
    print(message)

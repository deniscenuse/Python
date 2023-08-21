def calculate(num1, num2, operation):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return None

    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        return num1 // num2
    else:
        return None


result = None

while True:
    print("Select an operation to perform:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. CLEAR RESULT")
    print("6. EXIT")

    operation = input()

    if operation == "6":
        print("Exiting the calculator.")
        break

    if operation == "5":
        result = None
        print("Result has been cleared.")
        print()
        continue

    if operation in ["1", "2", "3", "4"]:
        num1 = str(result) if result is not None else None

        while num1 is None:
            num1 = input("Enter first number: ")
            if not num1.isdigit():
                print("That is not a number, please enter a number.")
                num1 = None

        num2 = None

        while num2 is None:
            num2 = input("Enter second number: ")
            if not num2.isdigit():
                print("That is not a number, please enter a number.")
                num2 = None

        result = calculate(num1, num2, operation)

        if result is not None:
            print("The result is " + str(result))
        else:
            print("Invalid Entry")
            print()
    else:
        print("Invalid Operation")
        print()

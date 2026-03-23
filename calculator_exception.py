while True:
    print("\n--------- MENU ---------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        print("Exiting... 👋")
        break

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
            print(f"Sum is: {num1 + num2}")

        elif choice == "2":
            print(f"Subtraction is: {num1 - num2}")

        elif choice == "3":
            print(f"Multiplication is: {num1 * num2}")

        elif choice == "4":
            print(f"Division is: {num1 / num2}")

        elif choice == "5":
            print(f"Modulus is: {num1 % num2}")

        else:
            print("Invalid choice ❌")

    except ZeroDivisionError:
        print("Cannot divide by zero ❌")

    except ValueError:
        print("Please enter valid numbers ❌")
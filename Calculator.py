# ==========================
#      SIMPLE CALCULATOR
#        CodSoft Task 2
# ==========================

def calculator():
    print("\n" + "=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        try:
            # Input numbers
            num1 = float(input("\nEnter First Number : "))
            num2 = float(input("Enter Second Number: "))

            # Menu
            print("\nChoose Operation")
            print("-------------------------")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Modulus (%)")
            print("6. Power (**)")
            print("7. Floor Division (//)")
            print("-------------------------")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                result = num1 + num2
                print(f"\nResult = {result}")

            elif choice == "2":
                result = num1 - num2
                print(f"\nResult = {result}")

            elif choice == "3":
                result = num1 * num2
                print(f"\nResult = {result}")

            elif choice == "4":
                if num2 == 0:
                    print("\nError! Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"\nResult = {result}")

            elif choice == "5":
                if num2 == 0:
                    print("\nError! Cannot perform modulus by zero.")
                else:
                    result = num1 % num2
                    print(f"\nResult = {result}")

            elif choice == "6":
                result = num1 ** num2
                print(f"\nResult = {result}")

            elif choice == "7":
                if num2 == 0:
                    print("\nError! Floor division by zero is not allowed.")
                else:
                    result = num1 // num2
                    print(f"\nResult = {result}")

            else:
                print("\nInvalid Choice!")
                continue

            again = input("\nDo another calculation? (y/n): ").lower()

            if again != "y":
                print("\nThank you for using the Calculator!")
                break

        except ValueError:
            print("\nInvalid Input! Please enter numeric values.")


calculator()
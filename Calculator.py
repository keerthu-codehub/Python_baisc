import math

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder (Modulus)")
print("6. Exponentiation")
print("7. Square Root")

choice = input("Enter choice (1-7): ")

if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        print("Result:", num1 / num2 if num2 != 0 else "Error! Division by zero.")
    elif choice == '5':
        print("Result:", num1 % num2)
    elif choice == '6':
        print("Result:", num1 ** num2)

elif choice == '7':
    num = float(input("Enter the number: "))
    if num >= 0:
        print("Result:", math.sqrt(num))
    else:
        print("Error! Cannot take square root of a negative number.")

else:
    print("Invalid choice")

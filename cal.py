def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

def floordivision(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Cannot perform floor division by zero."

def modulus(a, b):
    return a % b

def exponentiation(a, b):
    return a ** b

print("CLI Calculator")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Floor Division (//)\n6. Modulus (%)\n7. Exponentiation (**)\n8. Exit")
    choice = input("Enter choice (1-8): ")
    if choice == '8':
        print("Invalid choice")
        break
    elif choice in ['1','2','3','4','5','6','7']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {floordivision(num1, num2)}")
        elif choice == '6':
            print(f"Result: {modulus(num1, num2)}")
        elif choice == '7':
            print(f"Result: {exponentiation(num1, num2)}")
    else:
        print("Invalid choice.")
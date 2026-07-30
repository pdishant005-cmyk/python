# Program to perform Arithmetic, Relational, and Logical Operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


print("\n--- Arithmetic Operations ---")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Floor Division =", a // b)
print("Exponent =", a ** b)

# Relational Operators
print("\n--- Relational Operations ---")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
print("\n--- Logical Operations ---")
print("(a > 0 and b > 0) :", a > 0 and b > 0)
print("(a > 0 or b > 0)  :", a > 0 or b > 0)
print("not(a > b)        :", not(a > b))
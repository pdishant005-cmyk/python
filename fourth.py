# String Operations in Python
text = input("Enter a string: ")

print("Original String:", text)
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])
print("Reverse String:", text[::-1])

name = input("Enter your name: ")
print("Welcome, {}!".format(name))
print(f"Hello, {name}!")

print("Upper Case:", text.upper())
print("Lower Case:", text.lower())
print("Length:", len(text))
print("Replace 'a' with '@':", text.replace('a', '@'))
print("Count of 'a':", text.count('a'))
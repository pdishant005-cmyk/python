# Program to iterate over List, String and Dictionary

# 1. Iterate over a List
fruits = ["Apple", "Banana", "Mango"]

print("List:")
for fruit in fruits:
    print(fruit)

name = "Python"
print("\nString:")
for char in name:
    print(char)
    
student = {
    "Name": "Dishant",
    "Age": 21,
    "Course": "MCA"
}

print("\nDictionary:")
for key, value in student.items():
    print(key, ":", value)
# Create a dictionary
student = {
    "Name": "Dishant",
    "Age": 20,
    "Course": "BCA"
}

# Display dictionary
print("Student Details:")
print(student)


print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student["City"] = "Rajkot"
print("\nUpdated Dictionary:", student)

print("\nDictionary Elements:")
for key, value in student.items():
    print(key, ":", value)
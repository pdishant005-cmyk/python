def greet():
    print("Welcome to Python Programming!")


def add(a, b):
    print("Sum =", a + b)


def student(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)


def details(name, age):
    print("Name:", name)
    print("Age:", age)

greet()
add(10, 20)
student("Dishant")
student("Rahul", "MCA")
details(age=20, name="Amit")
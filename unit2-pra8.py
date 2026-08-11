x = 10
def outer_function():
    y = 20

    def inner_function():
        z = 30

        nonlocal y
        y = y + 5

        print("Local variable z =", z)
        print("Nonlocal variable y =", y)
        print("Global variable x =", x)

    inner_function()

outer_function()

print("Global variable x =", x)
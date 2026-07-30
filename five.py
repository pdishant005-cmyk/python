
numbers = [10, 20, 30, 40, 50]


print("First Element:", numbers[0])
print("Last Element:", numbers[-1])


print("First Three Elements:", numbers[:3])
print("Last Two Elements:", numbers[-2:])

numbers.append(60)
numbers.remove(20)
print("Updated List:", numbers)


squares = [x**2 for x in numbers]
print("Squares:", squares)
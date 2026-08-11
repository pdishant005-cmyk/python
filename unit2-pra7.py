

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print("List Comprehension:")
print(squares)

numbers = [1, 2, 3, 4, 5]

square_dict = {num: num * num for num in numbers}

print("\nDictionary Comprehension:")
print(square_dict)

numbers = [1, 2, 2, 3, 3, 4, 5]

square_set = {num * num for num in numbers}

print("\nSet Comprehension:")
print(square_set)
numbers = [10, 20, 30, 40, 50]

print("Iterable:")
for num in numbers:
    print(num)

numbers_iterator = iter(numbers)

print("\nIterator:")
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
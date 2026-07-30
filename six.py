t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("First Element:", t[0])
print("Last Element:", t[-1])
print("Tuple Length:", len(t))

s = {10, 20, 30, 40}

print("\nSet:", s)

s.add(50)
print("After Add:", s)

s.remove(20)
print("After Remove:", s)

print("Is 30 in Set?", 30 in s)
print("Set Length:", len(s))
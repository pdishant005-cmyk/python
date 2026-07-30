# Program to demonstrate data types and type casting
integer_num = 10
float_num = 3.14
string_val = "Python"
bool_val = True


print("Integer:", integer_num, "Type:", type(integer_num))
print("Float:", float_num, "Type:", type(float_num))
print("String:", string_val, "Type:", type(string_val))
print("Boolean:", bool_val, "Type:", type(bool_val))



a = float(integer_num)
print("Integer to Float:", a, "Type:", type(a))
b = int(float_num)
print("Float to Integer:", b, "Type:", type(b))
c = str(integer_num)
print("Integer to String:", c, "Type:", type(c))
d = int("25")
print("String to Integer:", d, "Type:", type(d))
e = bool(integer_num)
print("Integer to Boolean:", e, "Type:", type(e))
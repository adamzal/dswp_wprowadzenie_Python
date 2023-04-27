from timeit import timeit

char_array = """['a']*1000000"""
int_array = """[1]*1000000"""
float_array = """[.1]*1000000"""

char_list = """['a' for _ in range(1000000)]"""
int_list = """[1 for _ in range(1000000)]"""
float_list ="""[.1 for _ in range(1000000)]"""

print("char_array",timeit(char_array, number=100))
print("char_list",timeit(char_list, number=100))
print()
print("int_array",timeit(int_array, number=100))
print("int_list",timeit(int_list, number=100))
print()
print("float_array",timeit(float_array, number=100))
print("float_list",timeit(float_list, number=100))
"""
Копирование
"""

a = [[1, 2], ["str", "str"]]
b = a
b[0].append(3)
# print(a)
# print(b)
print(b[0] is a[0])


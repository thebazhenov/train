"""
Типы данных
"""


# 1
a = [1, 2, 3]
b = a
b.append(4)
# print(a)
# print(a is b)


# 2
a = 10
b = a
# print(a is b)
b += 5
# print(a)
# print(b)


#3
# data = {
#     ([1, 2, 3]): "a",
#     (1, 2, 3): "b"
# }
# print(data)


#4
a = (1, [2, 3])
# a[1].append(4)
# print(a)


#5
a = [1, 2, 2, 3]
b = set(a)
# print(len(a), len(b))

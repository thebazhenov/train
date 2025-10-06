"""
Области видимости
"""

x = 5


def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    inner()
    print(x)

# outer()
# print(x)
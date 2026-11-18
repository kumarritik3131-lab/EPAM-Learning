# Butterfly pattern using stars

n = 5

# Upper wings
for i in range(1, n + 1):
    left = "*" * i
    middle = " " * (2 * (n - i))
    right = "*" * i
    print(left + middle + right)

# Lower wings
for i in range(n - 1, 0, -1):
    left = "*" * i
    middle = " " * (2 * (n - i))
    right = "*" * i
    print(left + middle + right)

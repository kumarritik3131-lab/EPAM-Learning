
# Diamond pattern using stars
# Change n to control the height of the upper half.

n = 5

# Upper half, including the middle row
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

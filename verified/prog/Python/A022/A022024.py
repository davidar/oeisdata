def a(n):
    if n == 0: return 6
    prev_1, prev_2 = 66, 6
    for i in range(2, n + 1):
        prev_2, prev_1 = prev_1, (prev_1 ** 2) // prev_2 + 1
    return prev_1 # _Paul Muljadi_, Feb 12 2024
print([a(n) for n in range(30)])

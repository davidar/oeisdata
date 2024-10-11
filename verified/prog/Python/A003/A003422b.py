def a(n):
    if n == 0: return 0
    s = f = 1
    for k in range(1, n):
        f *= k
        s += f
    return round(s)
print([a(n) for n in range(24)])  # _Peter Luschny_, Mar 05 2024
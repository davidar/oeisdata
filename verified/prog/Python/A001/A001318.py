def a(n):
    p = n % 2
    return (n + p)*(3*n + 2 - p) >> 3
print([a(n) for n in range(60)])  # _Peter Luschny_, Jul 15 2022
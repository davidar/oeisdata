def encode(n):
    if n == 0: return "0"
    c, C = "", 1
    while n > 0:
        b = bin(n)[3:]
        c = b + c
        if (m := len(b)) > 0: C += 1
        n = m
    c = "1" * C + "0" + c
    return c
a = lambda n: int(encode(n),2) # _Darío Clavijo_, Aug 23 2024
print([a(n) for n in range(30)])

def a(n):
    k = 0
    while n > 0 and n%3 == 0: n //= 3; k += 1
    return k
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Aug 06 2021
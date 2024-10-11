def a(n):
    if n == 1: return 1023456789
    a020667n = 2
    while not(len(set(str(a020667n**n))) == 10): a020667n += 1
    return a020667n**n
print([a(n) for n in range(1, 16)]) # _Michael S. Branicky_, Jul 04 2021
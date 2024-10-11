def a(n):
    if n == 1: return 1023456789
    an = 2
    while not(len(set(str(an**n))) == 10): an += 1
    return an
print([a(n) for n in range(1, 90)]) # _Michael S. Branicky_, Jul 04 2021
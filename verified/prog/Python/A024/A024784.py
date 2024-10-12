from sympy import isprime
def afull():
    prime9strings, alst = list("2357"), []
    while len(prime9strings) > 0:
        alst.extend(sorted(int(p) for p in prime9strings))
        candidates = set(d+p for p in prime9strings for d in "12345678")
        prime9strings = [c for c in candidates if isprime(int(c, 9))]
    return alst
print(afull()) # _Michael S. Branicky_, Apr 27 2022
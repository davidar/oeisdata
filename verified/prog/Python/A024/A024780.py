from sympy import isprime
def afull():
    prime_strings, alst = list("23"), []
    while len(prime_strings) > 0:
        alst.extend(sorted(int(p) for p in prime_strings))
        candidates = set(d+p for p in prime_strings for d in "1234")
        prime_strings = [c for c in candidates if isprime(int(c, 5))]
    return alst
print(afull()) # _Michael S. Branicky_, Apr 27 2022
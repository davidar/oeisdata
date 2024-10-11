from sympy import isprime
def aupto(limit):
    alst, k, d = [], 1, 7
    while d <= limit:
        if isprime(d): alst.append(d)
        k += 1; d = 1+3*k*(k+1)
    return alst
print(aupto(34000)) # _Michael S. Branicky_, Jul 19 2021
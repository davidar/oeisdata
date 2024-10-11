from sympy import primerange
def aupton(N): # compute terms a(0)..a(N)
    V = [1 for j in range(N+1)]
    for i in primerange(2, N+1):
        for j in range(N, i-1, -1):
            hi = V[j]
            pp = i
            while pp <= j:
                hi = max((pp if j==pp else V[j-pp]*pp), hi)
                pp *= i
            V[j] = hi
    return V
print(aupton(47)) # _Michael S. Branicky_, Oct 09 2022 after _Joerg Arndt_
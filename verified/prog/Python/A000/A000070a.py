from itertools import accumulate
def A000070iter(n):
    L = [0]*n; L[0] = 1
    def numpart(n):
        S = 0; J = n-1; k = 2
        while 0 <= J:
            T = L[J]
            S = S+T if (k//2)%2 else S-T
            J -= k  if (k)%2 else k//2
            k += 1
        return S
    for j in range(1, n): L[j] = numpart(j)
    return accumulate(L)
print(list(A000070iter(100))) # _Peter Luschny_, Aug 30 2019
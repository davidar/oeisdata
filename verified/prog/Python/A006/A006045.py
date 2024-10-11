# see link for faster version
from itertools import product
def mmm2(A, B, modder): # matrix multiply modulo for 2x2
  return ((A[0]*B[0]+A[1]*B[2])%modder, (A[0]*B[1]+A[1]*B[3])%modder,
          (A[2]*B[0]+A[3]*B[2])%modder, (A[2]*B[1]+A[3]*B[3])%modder)
def order(A, modder):
  Ak, k = A, 1
  while mmm2(Ak, Ak, modder) != Ak: Ak, k = mmm2(Ak, A, modder), k+1
  return k
def a(n): return sum(order(A, n) for A in product(range(n), repeat=4))
print([a(n) for n in range(1, 12)]) # _Michael S. Branicky_, Jan 26 2021
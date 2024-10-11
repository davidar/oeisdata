# The objective of this implementation is efficiency.
# n -> [a(0), a(1), ..., a(n)] for n > 0.
from fractions import Fraction
def A000367_list(n):  # Bernoulli numerators
    T = [0 for i in range(1, n+2)]
    T[0] = 1; T[1] = 1
    for k in range(2, n+1):
        T[k] = (k-1)*T[k-1]
    for k in range(2, n+1):
        for j in range(k, n+1):
            T[j] = (j-k)*T[j-1]+(j-k+2)*T[j]
    a = 0; b = 6; s = 1
    for k in range(1, n+1):
        T[k] = s*Fraction(T[k]*k, b).numerator
        h = b; b = 20*b - 64*a; a = h; s = -s
    return T
print(A000367_list(100)) # _Peter Luschny_, Aug 09 2011
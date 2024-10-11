from sympy import cacheit
from sympy.ntheory import divisor_sigma
@cacheit
def A000219(n):
    if n <= 1:
        return 1
    return sum(A000219(n - k) * divisor_sigma(k, 2) for k in range(1, n + 1)) // n
print([A000219(n) for n in range(20)])
# _R. J. Mathar_, Oct 18 2009
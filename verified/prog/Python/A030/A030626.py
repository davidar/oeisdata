from sympy import divisor_count
isok = lambda n: divisor_count(n) == 8
print([n for n in range(1, 400) if isok(n)]) # _Darío Clavijo_, Oct 17 2023
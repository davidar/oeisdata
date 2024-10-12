from sympy import divisor_sigma
def A000594(n): return n**4*divisor_sigma(n)-24*((m:=n+1>>1)**2*(0 if n&1 else (m*(35*m - 52*n) + 18*n**2)*divisor_sigma(m)**2)+sum((i*(i*(i*(70*i - 140*n) + 90*n**2) - 20*n**3) + n**4)*divisor_sigma(i)*divisor_sigma(n-i) for i in range(1,m))) # _Chai Wah Wu_, Nov 08 2022
print([A000594(n) for n in range(1,31)])

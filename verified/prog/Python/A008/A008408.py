from sympy import divisor_sigma
def A008408(n): return 65520*(divisor_sigma(n,11)-(n**4*divisor_sigma(n)-24*((m:=n+1>>1)**2*(0 if n&1 else (m*(35*m - 52*n) + 18*n**2)*divisor_sigma(m)**2)+sum((i*(i*(i*(70*i - 140*n) + 90*n**2) - 20*n**3) + n**4)*divisor_sigma(i)*divisor_sigma(n-i) for i in range(1,m)))))//691 if n else 1 # _Chai Wah Wu_, Nov 17 2022
print([A008408(n) for n in range(30)])

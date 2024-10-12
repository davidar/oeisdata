def d(n,m): return not n % m
def A007569(n): return 2 if n == 2 else n*(42*d(n,12) - 144*d(n,120) + 60*d(n,18) - 96*d(n,210) + 35*d(n,24)- 38*d(n,30) - 82*d(n,42) - 330*d(n,60) - 144*d(n,84) - 96*d(n,90)) + (n**4 - 6*n**3 + 11*n**2 + 18*n -d(n,2)*(5*n**3 - 45*n**2 + 70*n - 24) - 36*d(n,4)*n - 4*d(n,6)*n*(45*n - 262))//24 # _Chai Wah Wu_, Mar 08 2021
print([A007569(n) for n in range(1,31)])

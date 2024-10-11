from math import comb
def A006356(n): return sum(comb(j,a)*comb(k,j)*comb(n+k-i,k-1)*(-1 if j-k&1 else 1) for k in range(1,n+2) for i in range(k,n+2) for j in range(k+1) if (a:=-3*k+2*j+i)>=0) # _Chai Wah Wu_, Feb 19 2024
print([A006356(n) for n in range(30)])

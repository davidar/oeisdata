from gmpy2 import divexact
A006318 = [1, 2]
for n in range(3,10**3):
    A006318.append(int(divexact(A006318[-1]*(6*n-9)-(n-3)*A006318[-2],n)))
# _Chai Wah Wu_, Sep 01 2014
print(A006318)

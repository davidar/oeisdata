A000078 = [0,0,0,1]
for n in range(4, 100):
    A000078.append(A000078[n-1]+A000078[n-2]+A000078[n-3]+A000078[n-4])
# _Chai Wah Wu_, Aug 20 2014
print(A000078)

from gmpy2 import is_square, isqrt
from itertools import combinations, product
A016069_list = []
for g in range(2,10):
    n = 2**g-1
    for x in combinations('0123456789',2):
        for i,y in enumerate(product(x,repeat=g)):
            if i > 0 and i < n and y[0] != '0':
                z = int(''.join(y))
                if is_square(z):
                    A016069_list.append(int(isqrt(z)))
A016069_list = sorted(A016069_list) # _Chai Wah Wu_, Nov 03 2014
print(A016069_list)

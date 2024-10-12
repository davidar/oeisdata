from sympy import integer_log
def A022331(n):
    m = 1<<n
    return sum((m//3**i).bit_length() for i in range(integer_log(m,3)[0]+1)) # _Chai Wah Wu_, Sep 16 2024
print([A022331(n) for n in range(30)])

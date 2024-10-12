from mpmath import mp
def A000796(n):
    if n >= len(A000796.str): mp.dps = n*6//5+50; A000796.str = str(mp.pi-5/mp.mpf(10)**mp.dps)
    return int(A000796.str[n if n>1 else 0])
A000796.str = '' # _M. F. Hasler_, Jun 21 2022
print([A000796(n) for n in range(1,31)])

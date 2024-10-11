from mpmath import mp
def A014777(n):
    if not (i := A014777.pos.get(n, 0)):
        d = str(n); s = 2 # starting position for search
        while (i := A014777.pi.find(d, s)) < 1:
            s = max(len(A014777.pi) - len(d), 2)
            with mp.workdps(s + 99 if s < 500 else s*6//5): # new precision
                A014777.pi = str(mp.pi - 5/mp.mpf(10)**mp.dps) # don't round
        i -= 1; A014777.pos[n] = i
    return i
A014777.pi = ''; A014777.pos = {} # _M. F. Hasler_, Jun 21 2022
print([A014777(n) for n in range(30)])

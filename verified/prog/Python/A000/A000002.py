# For explanation see link.
def Kolakoski():
    x = y = -1
    while True:
        yield [2,1][x&1]
        f = y &~ (y+1)
        x ^= f
        y = (y+1) | (f & (x>>1))
K = Kolakoski()
print([next(K) for _ in range(100)]) # _David Eppstein_, Oct 15 2016
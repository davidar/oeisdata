from itertools import count, takewhile
def F(f=1, g=1):
    while True:
        f, g = g, f+g;
        yield f
def a(n):
    return sum(1 for f in takewhile(lambda x: x<=n, F()) if n%f == 0)
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Apr 03 2023
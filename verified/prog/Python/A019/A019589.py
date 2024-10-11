import itertools
def a019589(n):
    s = set()
    for p in itertools.permutations(range(n)):
        s.add(tuple(sorted([k - p[k] for k in range(n)])))
    return len(s)
print([a019589(n) for n in range(10)])
# _Bert Dobbelaere_, Jan 19 2019
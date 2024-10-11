def a(n): return int("".join(sorted(str(n), reverse=True)))
print([a(n) for n in range(73)]) # _Michael S. Branicky_, Feb 21 2021
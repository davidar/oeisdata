def agen(rows):
    for n in range(1, rows+1): yield from range(n, 0, -1)
print([an for an in agen(13)]) # _Michael S. Branicky_, Aug 17 2021
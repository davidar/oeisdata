A011754 = lambda n: (3**n).bit_count() # _M. F. Hasler_, Apr 17 2024
print([A011754(n) for n in range(30)])

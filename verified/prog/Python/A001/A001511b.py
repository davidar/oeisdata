A001511 = lambda n: (n&-n).bit_length() # _M. F. Hasler_, Apr 09 2020
print([A001511(n) for n in range(1,31)])

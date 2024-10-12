def ok(n):
    mask, c = 3, 0
    for i in range(n.bit_length() >> 1):
        if (mask&n) >> (i << 1) == 2: c += 1
        mask <<= 2
    return c == 2
print([k for k in range(227) if ok(k)]) # _Michael S. Branicky_, Oct 26 2022
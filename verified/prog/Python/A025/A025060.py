def aupto(N):
    aset = set()
    for i in range(1, N-1):
        for j in range(i+1, N//i + 1):
            p, s = i*j, i+j
            for k in range(j+1, (N-p)//s + 1):
                aset.add(p + s*k)
    return sorted(aset)
print(aupto(109)) # _Michael S. Branicky_, Nov 14 2021
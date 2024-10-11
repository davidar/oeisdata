def aupton(nn):
    ans, f, g, k = dict(), 0, 1, 0
    while len(ans) < nn+1:
        sf = str(f)
        for i in range(1, len(sf)+1):
            if int(sf[:i]) > nn:
                break
            if sf[:i] not in ans:
                ans[sf[:i]] = k
        f, g, k = g, f+g, k+1
    return [int(ans[str(i)]) for i in range(nn+1)]
print(aupton(70)) # _Michael S. Branicky_, Jul 08 2022
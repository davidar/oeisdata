def aupto(nn):
    S, Fnm2, Fnm1 = [1, 2], 1, 2
    while len(S) < nn+1:
        S += S[:min(Fnm2, nn+1-len(S))]
        Fnm2, Fnm1 = Fnm1, Fnm1+Fnm2
    return S
print(aupto(104)) # _Michael S. Branicky_, Jun 06 2022
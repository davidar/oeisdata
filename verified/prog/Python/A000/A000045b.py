def A000045(n, F=[0,1]):
    F.extend(sum(F[-2:])for _ in range(n-len(F)+1)); return F[n] # _M. F. Hasler_, Feb 17 2023
print([A000045(n) for n in range(30)])

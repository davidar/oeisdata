def A029744(n):
    if n == 1: return 1
    elif n % 2 == 0: return 2**(n//2)
    else: return 3 * 2**((n-3)//2) # _Karl-Heinz Hofmann_, Sep 08 2022
print([A029744(n) for n in range(1,31)])

def A014707(n):
    s = bin(n+1)[2:]
    m = len(s)
    i = s[::-1].find('1')
    return int(s[m-i-2]) if m-i-2 >= 0 else 0 # _Chai Wah Wu_, Apr 08 2021
print([A014707(n) for n in range(30)])

def A023109(n):
    if n > 0:
        k = 0
        while True:
            m = k
            for i in range(n):
                if str(m) == str(m)[::-1]:
                    break
                m += int(str(m)[::-1])
            else:
                if str(m) == str(m)[::-1]:
                    return k
            k += 1
    else:
        return 0
# _Chai Wah Wu_, Feb 08 2015
print([A023109(n) for n in range(30)])

def isUlam(n, h, u, r):
    if h == 2: return False
    hu = u[0]; hr = r[0]
    if hr <= hu: return h == 1
    if hr + hu > n: r = r[1:]
    elif hr + hu < n: u = u[1:]
    else: h += 1; r = r[1:]; u = u[1:]
    return isUlam(n, h, u, r)
def UlamList(length):
    u = [1, 2]; r = [2, 1]; n = 2
    while len(u) < length:
        n += 1
        if isUlam(n, 0, u[:], r[:]):
            u.append(n); r.insert(0, n)
    return u
print(UlamList(59)) # _Peter Luschny_, Apr 06 2019
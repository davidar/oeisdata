from itertools import count, takewhile
def cands(n, d):
    return takewhile(lambda x: x<=n, (d**i for i in count(1)))
def handsome(s, t):
    if s == "":
        return t == 0
    if s[0] in "01":
        return handsome(s[1:], t - int(s[0]))
    return any(handsome(s[1:], t - p) for p in cands(t, int(s[0])))
def ok(n):
    return n and handsome(str(n), n)
print(list(filter(ok, range(1035)))) # _Michael S. Branicky_, Aug 18 2021
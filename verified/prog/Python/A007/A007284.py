allowed = ("0", "1", "3", "8")
def a(n):
    return all(x in allowed for x in str(n))
print([i for i in range(50000) if a(i)])
# _Indranil Ghosh_, Feb 03 2017
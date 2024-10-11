# Works in Sage also.
A000108 = [1]
for n in range(1000):
    A000108.append(A000108[-1]*(4*n+2)//(n+2)) # _Günter Rote_, Nov 08 2023
print(A000108)

from sympy import divisor_count
A002182_list, r = [], 0
for i in range(1,10**4):
    d = divisor_count(i)
    if d > r:
        r = d
        A002182_list.append(i) # _Chai Wah Wu_, Mar 23 2015
print(A002182_list)

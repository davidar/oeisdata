from re import split
A022510_list, l = [6], '6'
for _ in range(10):
    l = ''.join(str(len(d))+d[0] for d in split('(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)',l[::-1]) if d)
    A022510_list.append(int(l)) # _Chai Wah Wu_, Jan 02 2015
print(A022510_list)

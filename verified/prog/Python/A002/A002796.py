A002796_list = []
for i in range(1,10**5):
    for d in set(str(i)):
        if d != '0' and i % int(d):
            break
    else:
        A002796_list.append(i) # _Chai Wah Wu_, Mar 26 2021
print(A002796_list)

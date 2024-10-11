A005487_list = [0,4]
for i in range(101-2):
    n, flag = A005487_list[-1]+1, False
    while True:
        for j in range(i+1,0,-1):
            m = 2*A005487_list[j]-n
            if m in A005487_list:
                break
            if m < A005487_list[0]:
                flag = True
                break
        else:
            A005487_list.append(n)
            break
        if flag:
            A005487_list.append(n)
            break
        n += 1 # _Chai Wah Wu_, Jan 05 2016
print(A005487_list)

A000139_list = [2]
for n in range(1,30):
    A000139_list.append(3*(3*n-2)*(3*n-1)*A000139_list[-1]//(2*n+2)//(2*n+1)) # _Chai Wah Wu_, Apr 02 2021
print(A000139_list)

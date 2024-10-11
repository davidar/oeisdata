from sympy import isprime
A002385 = [*filter(isprime, (int(str(x) + str(x)[-2::-1]) for x in range(10**5)))]
A002385.insert(4, 11)  # _Yunhan Shi_, Mar 03 2023
print(A002385)

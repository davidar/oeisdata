def A000032_gen(): # generator of terms
    a, b = 2, 1
    while True:
        yield a
        a, b = b, a+b
it = A000032_gen()
A000032_list = [next(it) for _ in range(50)] # _Cole Dykstra_, Aug 02 2022
print(A000032_list)

def A000125_gen():  # generator of terms
    a, b, c = 1, 1, 1
    while True:
        yield a
        a, b, c = a+b, b+c, c+1
it = A000125_gen()
A000125_list = [next(it) for _ in range(50)]  # _Cole Dykstra_, Aug 03 2022
print(A000125_list)

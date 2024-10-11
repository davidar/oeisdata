def A000297_gen():  # generator of terms
    a, b, c = 0, 4, 4
    while True:
        yield a
        a, b, c = a+b, b+c, c+1
it = A000297_gen()
A000297_list = [next(it) for _ in range(50)]  # _Cole Dykstra_, Aug 05 2022
print(A000297_list)

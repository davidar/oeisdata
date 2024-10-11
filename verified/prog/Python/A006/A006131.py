def A006131_list(n):
    list = [1, 1] + [0] * (n - 2)
    for i in range(2, n):
        list[i] = list[i - 1] + 4 * list[i - 2]
    return list
print(A006131_list(29)) # _M. Eren Kesim_, Jul 19 2021
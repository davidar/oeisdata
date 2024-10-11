def A000699_list(n):
    list = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        list[i] = (i - 1) * sum(list[j] * list[i - j] for j in range(1, i))
    return list
print(A000699_list(22)) # _M. Eren Kesim_, Jun 23 2021
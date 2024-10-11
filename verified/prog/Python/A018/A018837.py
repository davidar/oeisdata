def a(n): return 3 if n == 1 else (n + n % 4) // 2 # _Elisha Hollander_, Aug 05 2021
print([a(n) for n in range(30)])

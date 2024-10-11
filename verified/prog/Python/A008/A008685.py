def a(n):
    y, m = 1 + (n-1)//12, (n-1)%12
    leap = int((y%4 == 0 and y%100 != 0) or y%400 == 0)
    return [31, 28+leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]
print([a(n) for n in range(1, 64)]) # _Michael S. Branicky_, Feb 04 2024
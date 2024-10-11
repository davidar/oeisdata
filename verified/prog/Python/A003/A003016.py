from math import isqrt # requires python3.8 or higher
def A003016(n):
    if n < 4: return[0,3,1,2][n]
    cnt = k = 2; r = isqrt(2*n)+1; C = r*(r-1)//2
    while True:
       while C < n and k < r//2:
          C *= r-k; k += 1; C //= k
       if C == n: cnt += 2 - (r == 2*k)
       if k >= r//2: return cnt
       C *= r-k; C //= r; r -= 1 # _M. F. Hasler_, Feb 16 2023
print([A003016(n) for n in range(30)])

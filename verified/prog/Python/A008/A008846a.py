# for an array from the beginning
from math import gcd, isqrt
hypothenuses_upto = 433
A008846 = set()
for x in range(2, isqrt(hypothenuses_upto)+1):
    for y in range(min(x-1, (yy:=isqrt(hypothenuses_upto-x**2))-(yy%2 == x%2)) , 0, -2):
        if gcd(x,y) == 1: A008846.add(x**2 + y**2)
print(A008846:=sorted(A008846)) # _Karl-Heinz Hofmann_, Sep 30 2024
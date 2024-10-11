from itertools import accumulate
def f(an, _): return (an//2)*((an+1)//2)
print(list(accumulate([5]*11, f))) # _Michael S. Branicky_, May 06 2021
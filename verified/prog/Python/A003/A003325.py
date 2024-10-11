from sympy import integer_nthroot
def aupto(lim):
  cubes = [i*i*i for i in range(1, integer_nthroot(lim-1, 3)[0] + 1)]
  sum_cubes = sorted([a+b for i, a in enumerate(cubes) for b in cubes[i:]])
  return [s for s in sum_cubes if s <= lim]
print(aupto(1343)) # _Michael S. Branicky_, Feb 09 2021
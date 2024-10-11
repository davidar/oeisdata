# from http://code.activestate.com/recipes/577821-integer-square-root-function/
def A000196(n):
  if n < 0:
    raise ValueError('only defined for nonnegative n')
  if n == 0:
    return 0
  a, b = divmod(n.bit_length(), 2)
  j = 2**(a+b)
  while True:
    k = (j + n//j)//2
    if k >= j:
      return j
    j = k
print([A000196(n)for n in range(102)])
# _Jason Kimberley_, Nov 09 2016
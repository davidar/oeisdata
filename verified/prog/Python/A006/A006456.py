from gmpy2 import is_square
class Memoize:
    def __init__(self, func):
        self.func=func
        self.cache={}
    def __call__(self, arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg)
        return self.cache[arg]
@Memoize
def a(n): return 1 if n==0 else sum([a(n - k) for k in range(1, n + 1) if is_square(k)])
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jul 28 2017, after _David W. Wilson_'s formula
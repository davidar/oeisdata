from fractions import Fraction
nums = [17, 78, 19, 23, 29, 77, 95, 77,  1, 11, 13, 15, 1, 55] # A202138
dens = [91, 85, 51, 38, 33, 29, 23, 19, 17, 13, 11,  2, 7,  1] # A203363
PRIMEGAME = [Fraction(num, den) for num, den in zip(nums, dens)]
def succ(n, program):
  for i in range(len(program)):
    if (n*program[i]).denominator == 1: return (n*program[i]).numerator
def orbit(start, program, steps):
  orb = [start]
  for s in range(1, steps): orb.append(succ(orb[-1], program))
  return orb
print(orbit(2, PRIMEGAME, steps=42)) # _Michael S. Branicky_, Feb 15 2021
from sympy import E
def aupto(digit_limit):
  alst, estr = [], str(E.n(digit_limit)).replace(".", "")
  prevlen, prevstr, suffix = 0, "", estr
  while len(suffix) > prevlen + 1:
    if suffix[:prevlen] > prevstr: idx = prevlen
    else: idx = prevlen + 1
    while suffix[idx] == '0':
      idx += 1
      if idx > len(suffix): break # end of string reached
    anstr, suffix = suffix[:idx], suffix[idx:]
    prevstr, prevlen = anstr, len(anstr)
    assert anstr[0] != '0'
    alst.append(int(anstr))
  return alst
print(aupto(220)) # _Michael S. Branicky_, Feb 07 2021
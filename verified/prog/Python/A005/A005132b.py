def recaman(n):
  seq = []
  for i in range(n):
    if(i == 0): x = 0
    else: x = seq[i-1]-i
    if(x>=0 and x not in seq): seq+=[x]
    else: seq+=[seq[i-1]+i]
  return seq
print(recaman(1000)) # _Ely Golden_, Jun 14 2018
def aupton(nn):
  alst, R = [1], {0: {1}} # R[n] is set reachable using n+1 1's (n ops)
  for n in range(1, nn):
    R[n]  = set(a+b for i in range(n//2+1) for a in R[i] for b in R[n-1-i])
    R[n] |= set(a*b for i in range(n//2+1) for a in R[i] for b in R[n-1-i])
    alst.append(min(R[n] - R[n-1]))
  return alst
print(aupton(35)) # _Michael S. Branicky_, Jun 08 2021
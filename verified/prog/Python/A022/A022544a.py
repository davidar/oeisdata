def aupto(lim):
  squares = [k*k for k in range(int(lim**.5)+2) if k*k <= lim]
  sum2sqs = set(a+b for i, a in enumerate(squares) for b in squares[i:])
  return sorted(set(range(lim+1)) - sum2sqs)
print(aupto(199)) # _Michael S. Branicky_, Mar 06 2021
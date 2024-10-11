def aupto(lim):
  squares = [k*k for k in range(1, int(lim**.5)+2) if k*k <= lim]
  sum2sqs = set(a+b for i, a in enumerate(squares) for b in squares[i:])
  sum3sqs = set(a+b for a in sum2sqs for b in squares)
  return sorted(set(range(lim+1)) & (sum3sqs - sum2sqs - set(squares)))
print(aupto(142)) # _Michael S. Branicky_, Mar 06 2021
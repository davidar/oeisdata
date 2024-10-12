a=[1]; [a.append(a[-2]+a[-1] if n%2 else a[n//2-1]) for n in range(2, 75)]
print(a) # _Michael S. Branicky_, Jul 07 2022
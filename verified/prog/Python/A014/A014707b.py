def A014707(n): n+=1; h=n&-n; n=n&(h<<1); return int(n!=0)
print([A014707(n) for n in range(93)]) # _Michael S. Branicky_, Mar 29 2024 after _Joerg Arndt_
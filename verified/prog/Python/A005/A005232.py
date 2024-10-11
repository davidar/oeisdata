a=lambda n: sum((k//2+1)*((n-k)//2+1) for k in range((n-1)//2+1))+(n+1)%2*(((n//4+1)*(n//4+2))//2)  # _Gabriel Burns_, Nov 08 2016
print([a(n) for n in range(30)])

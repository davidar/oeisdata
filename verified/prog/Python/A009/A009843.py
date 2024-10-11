# The objective of this implementation is efficiency.
# n -> [a(0), a(1), ..., a(n)] for n > 0.
def A009843_list(n):
    S = [0 for i in range(n+1)]
    S[0] = 1
    for k in range(1, n+1):
        S[k] = k*S[k-1]
    for k in range(1, n+1):
        for j in range(k, n+1):
            S[j] = (j-k)*S[j-1]+(j-k+1)*S[j]
        S[k] = (2*k+1)*S[k]
    return S
print(A009843_list(10)) # _Peter Luschny_, Aug 09 2011
def A004176(n): return int(s) if (s:=str(n).replace('1','')) else 0 # _M. F. Hasler_, Jan 23 2023
print([A004176(n) for n in range(30)])

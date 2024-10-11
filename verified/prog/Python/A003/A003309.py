remainders = [0]
ludics = [2]
N_MAX = 313
for i in range(3, N_MAX) :
    ludic_index = 0
    while ludic_index < len(ludics) :
        ludic = ludics[ludic_index]
        remainder = remainders[ludic_index]
        remainders[ludic_index] = (remainder + 1) % ludic
        if remainders[ludic_index] == 0 :
            break
        ludic_index += 1
    if ludic_index == len(ludics) :
        remainders.append(0)
        ludics.append(i)
ludics = [1] + ludics
print(ludics)
# _Alexandre Herrera_, Aug 10 2023
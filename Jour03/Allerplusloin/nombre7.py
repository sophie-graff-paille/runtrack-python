#ch = "sophie"
#inv = ch[::-1]
#print(inv)

ch = "Sophie"
ch_reversed = ""
i = len(ch)

while i > 0:
    ch_reversed += ch[i-1]
    i = i - 1
print(ch_reversed)
L = [8,24,48,2,16]
long = len(L)
nbmultiples = 0
for i in range(long):
    if L[i] % 3 == 0:
        nbmultiples = nbmultiples + 1

print (nbmultiples)
L = [8,24,27,48,2,16, 9,7,84,91]
long = len(L)
sumpaire = 0
for i in range (long):
    if L[i] % 2 == 0:
        sumpaire = sumpaire + L[i]

print (sumpaire)
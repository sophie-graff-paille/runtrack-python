#L = [8,24,27,48,2,16,9,102,7,84,91]
#long = len(L)
#max = L[0]
#min = L[0]
#for i in range (long):
#    if L[i] > max:
#       max = L[i]
#    else:
#        if L[i] < min:
#            min = L[i]

#print(max,min)
L = [8,24,27,48,2,16,9,102,7,84,91]
def maximini(L):
    L.sort() #pour trier la liste
    return (L[-1],L[0])

print(maximini (L))
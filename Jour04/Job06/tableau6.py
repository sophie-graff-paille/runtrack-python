L=[2,5,6,8,12]
last = L[-1] #dernier élément de ma liste
L[-1] = L[0] #remplace le dernier par le premier
L[0] = last #remplace le premier par le dernier

print(L)
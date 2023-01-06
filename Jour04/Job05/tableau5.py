L=[2,5,6,8,12]
print(L[1])

def remplace():
    L.insert(3, L[2]+L[4])
    L.remove(L[4])
    return L[4]

print(remplace())
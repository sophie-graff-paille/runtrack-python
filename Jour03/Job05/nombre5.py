nbPremiers = 0
i = 2
while(nbPremiers<168):
    j = 2
    nbfound = False
    while(j <= i//2) and (nbfound == False):
        if (i%j == 0):
            nbfound = True
        else:
            j+= 1
    if nbfound == False:
        print(nbPremiers,i)
        nbPremiers+= 1
    i+= 1
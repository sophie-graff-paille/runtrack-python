ch = "abcdefghijklmnopqrstuvwxyz" * 10
i = 1
while i <= len(ch):
    print(ch[:i]) #les premiers caractères
    ch = ch[i:] #les caractères suivants
    i+= 1 #incrémentation d'une lettre à chaque boucle
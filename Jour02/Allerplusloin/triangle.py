import math
def triangle(a,b,c):
    if a + b >= c and a + c >= b and c + b >= a:
        result = "c'est un triangle"
        if a == b == c:
            result = "c'est un triangle équilatéral"
        elif a == b or b == c or c == a:
            if a**2 + b**2 == int(c**2):
                result = "c'est un triangle isocèle et rectangle"
            else:
                result = "c'est un triangle isocèle"
        elif a**2 + b**2 == c**2:
            result = "c'est un triangle rectangle"
    else:
        result = "ce n'est pas un triangle"
    print(result)

triangle(10,10,10)
triangle(10,6,10)
triangle(1,1,math.sqrt(2))
triangle(4,6,2)
triangle(3,4,11)

#Mathéo m'a aidée pour le rectangle isocèle lignes 1, 8, 9 et 20
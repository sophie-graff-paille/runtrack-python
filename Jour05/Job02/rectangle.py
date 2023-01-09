def rectangle(a,b):
    c='|'+'-'*(a-2)+'|\n'
    print(c+c.replace(*'- ')*(b - 2)+c)

largeur = int(input("Veuillez saisir la largeur désirée : "))
hauteur = int(input("Veuillez saisir la hauteur désirée : "))
rectangle(largeur,hauteur)
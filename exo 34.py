from random import *


def lance_de():
    hasard = randint(1,6)
    return hasard



def obtenir_six():
    compteur = 0
    resultat = 0
    while resultat != 6:
        resultat = lance_de()
        compteur = compteur + 1
    return compteur

val = obtenir_six()
print(val)
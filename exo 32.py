from random import *

def tirage_monopoly():
    resultat = 0
    for i in range(2):
        valeur = randint(1,6)
        resultat += valeur
    return resultat


val = tirage_monopoly()
print(val)
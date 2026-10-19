from math import *

def carre_parfait(n):
    valeur = sqrt(n)
    if valeur % 1 == 0:
        return True
    return False

def somme_carrés(n):
    somme = 0
    for i in range(1, n + 1):
        if carre_parfait(i):
            somme += i
    return somme

val = somme_carrés(100)
print(val)
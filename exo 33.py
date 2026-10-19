from random import *


def lance_de():
    hasard = randint(1,6)
    return hasard




def simulation(n):
    compteur = 0
    for i in range(n):
        if lance_de() == 6:
            compteur = compteur + 1
    return compteur / n

val = simulation(10)
print(val)
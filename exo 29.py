from math import *

def carre_parfait(n):
    valeur = sqrt(n)
    if valeur % 1 == 0:
        return True
    return False

val = carre_parfait(49)
print(val)
    
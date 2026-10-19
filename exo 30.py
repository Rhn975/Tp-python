from random import *

def pile_face():
    hasard = randint(1,2)
    if hasard == 1:
        return "pile"
    return "face"

val = pile_face()
print(val)
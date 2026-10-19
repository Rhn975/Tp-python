def est_pair(nombre):
    return nombre % 2 == 0

def syracuse(n,a):
    u = a
    for _ in range(n):
        if est_pair(u):
            u = u / 2
        else:
            u = 3*u + 1
    return u

def vol(a):
    valeur = [a]
    u = a
    n = 0
    while u != 1:
        n += 1
        u = syracuse(n,a)
        valeur.append(u)
    return valeur


def temp_vol(a):
    return len(vol(a)) - 1

def altitude(a):
    return max(vol(a))




val = altitude(15)
print(val)
    

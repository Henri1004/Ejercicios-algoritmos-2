#t es una lista de numeros deordenados q hay que ordenar
def orde_dicotomica(t):
    r = t

    for i in range(1,len(r)):
        a1 = r[i]

        izq = 0
        der = i
        while izq < der:
            medio = (izq+der)//2
            if a1 < r[medio]:
                der = medio
            else:
                izq = medio+1
        pos = izq
        r.insert(pos, a1)
        r.pop(i+1)
    return r

# ejemplo de uso:
t = [2,65,23,87,1,4,35]
c = orde_dicotomica(t)
print(c)

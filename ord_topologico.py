# t es una listas de tuplas, i representa la restriccion, y  j representa el orden, t se tiene que ordenar.

def ord_topologico(t):
    n = len(t)
    for i in range(n):
        ind_menor = i
        for j in range(i+1 , n):
            if (t[j][0]<t[ind_menor][0]) or (t[j][0]==t[ind_menor][0]) and (t[j][1]<t[ind_menor][1]):
                ind_menor = j
        t[i], t[ind_menor] = t[ind_menor], t[i]
    return t

#ejemplo de uso
a = [(1,1), (1,3), (1,2), (1,1), (1,3), (1,2), (1,9), (1,5), (1,7)]
print(ord_topologico(a))

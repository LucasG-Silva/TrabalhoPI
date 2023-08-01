from collections import deque

class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

class No:
    def __init__(self, nivel, inc, ex):
        self.nivel = nivel
        self.inc = inc
        self.ex = ex

def comp(a):
    return float(a.valor) / a.peso

def maxV(n, b, arr, t):
    carga=0
    valor=0
    inteira=True
    for i in n.inc:
        carga+=arr[i].peso
        valor+=arr[i].valor

    if(carga>b):
        return (0,True,0)

    j=0
    while j<t and carga+arr[j].peso<=b:
        if(not(j in n.inc) and not(j in n.ex)):
            carga+=arr[j].peso
            valor+=arr[j].valor

        j+=1

    while j<t:
        if(not(j in n.inc) and not(j in n.ex)):
            x=(b-carga)*arr[j].valor/arr[j].peso
            if(x!=0):
                valor+=x
                inteira=False

            break

        j+=1

    return (valor, inteira, j)

def mochila(b, arr, t):
    melhor=0
    arr = sorted(arr, key=comp, reverse= True)
    fila=deque([])
    u=No(0,[],[])
    fila.append(u)

    while len(fila)>0:
        u = fila[0]
        if(u.nivel==t):
            fila.popleft()
            continue

        val, inteira, k=maxV(u, b, arr, t)

        if(val<=melhor):
            fila.popleft()
            continue
        elif(inteira):
            melhor=val
        else:
            lInc=u.inc.copy()
            rEx=u.ex.copy()
            lInc.append(k)
            rEx.append(k)
            l=No(u.nivel+1, lInc, u.ex)
            r=No(u.nivel+1, u.inc, rEx)
            fila.append(l)
            fila.append(r)

        fila.popleft()


    return melhor

if __name__ == '__main__':
    b = 10
    arr = [Item(2, 40), Item(3.14, 50), Item(1.98, 100), Item(5, 95), Item(3, 30)]
    t = len(arr)
    print(mochila(b, arr, t))






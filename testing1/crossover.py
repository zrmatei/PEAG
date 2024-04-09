'''
                                        ****** CROSSOVER *****
                    AM NEVOIE DE  2 indivizi x1, x2 SI DE O PROB DE RECOMB, PC
1) Numere intregi
2) Numere binare
LA ASTEA 2 AM ACEEASI OPERATORI DE CROSSOVER:
    - c.unipunct ( fixez un punct pe o gena si modific in ambii indivizi )
    - c.multipunct ( fixez mai multe puncte )
    - c.uniform ( fixez pe toate punctele )
3) Numere reale - am nevoie si de un alpha aici
    - c. simplu ( schimb valorile de pe genele celor 2 indivzi de la i la j )
    - c. singular ( aleg o gena pentru ambii indivizi si le schimb valorile )
    - c. total ( schimb toate valorile de pe fiecare gena - practic fac un for )
4) Permutari ( -> sarim in aer daca pica permutari )
    - PMX
    - OCX
'''
import numpy as np


def c_unipunct(x1, x2, n):
    p = np.random.randint(0, n)
    c1 = x1.copy()
    c2 = x2.copy()
    c1[0:p] = x1[0:p]
    c1[p:n] = x1[p:n]
    c2[0:p] = x2[0:p]
    c2[p:n] = x1[p:n]
    return c1, c2


def c_multipunct(x1, x2, n):
    p1 = np.random.randint(0, n // 2)
    p2 = np.random.randint(p1, n)
    c1 = x1.copy()
    c2 = x2.copy()
    c1[p1:p2] = x2[p1:p2]
    c2[p1:p2] = x1[p1:p2]
    return c1, c2


def c_uniform(x1, x2, n):
    for i in range(n):
        p = np.random.randint(0, n)
        c1[p:n] = x1[p:n]
        c2[p:n] = x2[p:n]
    return c1, c2


def c_simplu(x1,x2,n,a):
    p1 = int(np.random.uniform(0, n//2) )
    p2 = int(np.random.uniform(n//2, n) )
    c1 = x1.copy()
    c2 = x2.copy()
    for i in range(p1, p2):
        c1[i] = a * x1[i] + ( (1 - a) * x2[i] )
        c2[i] = a * x2[i] + ( (1 - a ) * x1[i] )
    return c1,c2
def c_singular(x1, x2, n, alpha):
    p = int(np.random.uniform(0, n))
    c1 = x1.copy()
    c2 = x2.copy()
    c1[p] = alpha * x1[p] + ((1 - alpha) * x2[p])
    c2[p] = alpha * x2[p] + ((1 - alpha) * x1[p])
    return c1, c2

def c_total(x1,x2,n,a):
    p = int( np.random.uniform(0, n) )
    c1 = x1.copy()
    c2 = x2.copy()
    for i in range(0,n):
        c1[i] = a * x1[i] + ( (1 - a) * x2[i] )
        c2[i] = a * x2[i] + ( (1 - a) * x1[i] )
    return c1,c2

x1 = [1, 2, 3, 4, 5]
x2 = [6, 7, 8, 9, 10]
n = len(x1)
alpha = 0.2
c1, c2 = c_total(x1, x2, n, alpha)
print(c1, '\n', c2)

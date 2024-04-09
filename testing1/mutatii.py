'''
                                             *** MUTATII ***
                     SE FAC PE GENE, DECAT LA REP. PERMUTARI SE FAC PE  CROMOZOMI/INDIVIZI
                            AM NEVOIE DE GENA, DIM GENA SI PROB MUTATIE, PM
1) Nr intregi
    - resetare aleatoare ( inlocuiesc o valoare cu una aleatoare )
    - fluaj: +/- 1 ( inlocuiesc o valoare cu una mica )
2) Nr binare
    - negare ( 1 devine 0, 0 devine 1 )
3) Nr reale
    - m. uniforma -> acelasi lucru cu r. aleatoare
    - m. neuniforma -> acelasi lucru cu fluajul
4) Permutari
    - interschimbare ( iau 2 gene din pop (x), i, j si interschimb xi cu xj )
    - amestec ( iau 2 gene (i < j) si repozitionez aleator toate genele din intervalul i pana la j )
    - inserare -> sa nu pice ( iau 2 gene (i,j), mut xj pe xi + 1, restul genelor le mut cu o poz dupa xj nou)
    - inversiune -> sa NU pice
'''
import numpy as np

def m_reset(i, j): #2 gene
       gena = np.random.randint(i, j)
       return gena

def m_fluaj(gena, sigma, i, j):
    zgomot = np.random.randint(-sigma, sigma + 1)
    gena_m = gena + zgomot
    gena_m = min(max(gena_m, i), j) #ma asigur ca gena ramane in interval
    return gena_m

'''MUTATIA UNIFORMA E LA FEL CA CEA DE RESETARE ALEATOARE DE LA INTREGI, DOAR CA PUN .UNIFORM'''

def m_neuniforma(gena, sigma, i, j):
    zgomot = np.random.normal(0, sigma)
    gen_m = gena + zgomot
    if gen_m > j:
        gen_m = j
    elif gen_m < i:
        gen_m = i
    return gen_m

def m_negare(gena):
    gena_m = not gena
    return int(gena_m)

def m_interschimb(x, n): #se face pe cromozom, nu pe gena schimbarea
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    i = np.min(poz)
    j = np.max(poz)
    y = x.copy()
    y[i] = x[j]
    y[j] = x[i]
    return y

def m_amestec(x, n):
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    i = np.min(poz)
    j = np.max(poz)
    y = x.copy()
    #nu afectez genele din afara intervalului
    y[0:i] = x[0:i]
    y[j:n] = x[j:n]
    #afectez restul genelor din interval
    amestec = np.random.permutation(j-i)
    subsir = x[i:j]
    for k in range(j-i):
        y[i + k] = subsir[ amestec[k] ]
    return y


x = [1,3,2,4]
n = len(x)
y = m_amestec(x, n)
print(y)
def crossover_PMX(x1, x2, n):
    # generarea secventei de crossover
    poz = numpy.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = numpy.random.randint(0, n, 2)
    p1 = numpy.min(poz)
    p2 = numpy.max(poz)
    c1 = PMX(x2, x2, n, p1, p2)
    c2 = PMX(x2, x1, n, p1, p2)
    return c1, c2


# aplica PMX pe x1,x2 de dimensiune n, cu secventa de recombinare (p1,p2)
def PMX(x1, x2, n, p1, p2):
    # initializare copil - un vector cu toate elementele -1 - valori care s=sa nu fie in 0,...,n-1
    c = - numpy.ones(n, dtype=int)
    # copiaza secventa comuna in copilul c
    c[p1:p2 + 1] = x1[p1:p2 + 1]
    # analiza secventei comune - in permutarea y
    for i in range(p1, p2 + 1):
        # plasarea alelei a
        a = x2[i]
        if a not in c:
            curent = i
            plasat = False
            while not plasat:
                b = x1[curent]
                # poz=pozitia in care se afla b in y
                [poz] = [j for j in range(n) if x2[j] == b]
                if c[poz] == -1:
                    c[poz] = a
                    plasat = True
                else:
                    curent = poz
    # z= vectorul alelelor din y inca necopiate in c
    z = [x2[i] for i in range(n) if x2[i] not in c]
    # poz - vectorul pozitiilor libere in c - cele cu vaori -1
    poz = [i for i in range(n) if c[i] == -1]
    # copierea alelelor inca necopiate din y in c
    m = len(poz)
    for i in range(m):
        c[poz[i]] = z[i]
    return c


# operatorul OCX
# I: permutarile x,y de dimensiune n
# E: copiii rezultati c1,c2
def crossover_OCX(x, y, n):
    # generarea secventei de crossover
    poz = numpy.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = numpy.random.randint(0, n, 2)
    p1 = numpy.min(poz)
    p2 = numpy.max(poz)
    c1 = OCX(x, y, n, p1, p2)
    c2 = OCX(y, x, n, p1, p2)
    return c1, c2
def gen_pop(dim):
    pop = []
    for i in range(dim):
        flag = False
        while flag == False:
            x = np.random.randint(0, 2, 12) #am pun 12 pt ca am nevoie de 12 biti (2^12 = 4096) pt ca
                                          #fenotipul meu are val maxima 2500 (11 biti sunt prea putini, 2^11 = 2048)
            flag, qf = fitness(x) # qf - cal./scorul  fitness
        x = list(x)
        x.append(qf)
        pop.append(x)
    return pop

#daca nu am conditii in cerinta, sterg partea cu flag-ul

#//////////////

def binaryToDecimal(x): #x rep string-ul binar / individul
    n = len(x)
    nr = 0 #nr rep forma zecimala pe care o sa o folosesc ca sa adun toti bitii convertiti
    for i in range(n):
        nr += int(x[n-i-1]) * (2 ** i)
    return nr

#///////////////

def mutatie_populatie(pop, dim, n, c, probabilitate_m):
    pop_m = pop.copy()
    for i in range(dim):
        r = numpy.random.uniform(0, 1)
        if r <= probabilitate_m:
            x = pop[i][0:n].copy()
            y = m_perm_interschimbare(x, n)
            fitness = fitnessTSP(y, n, c)
            x = list(y)
            x = x + [fitness]
            pop_m[i] = x.copy()
    return pop_m

#/////////////// PT mutatie cand fac rep pe nr intregi/reale/binare (cand fac mutatie pe gene, nu pe individ)
def mutatie_pop(pop, dim, n, pm):
    copii_mut = []
    for i in range(dim):
        x = pop[i][0:n].copy()
        for j in range(n):
            if np.random.rand() < pm:
                x[j] = m_uniforma(0,1)
                copii_mut.append(x)
    return copii_mut

def crossover_populatie(pop, dim, n, c, v, cmax, probabilitate_crossover):
    copii = pop.copy()
    # populatia este parcursa astfel incat sunt selectati indivizii 0,1 apoi 2,3 s.a.m.d
    for i in range(0, dim - 1, 2):
        # selecteaza parintii
        x1 = pop[i][0:n].copy()
        x2 = pop[i + 1][0:n].copy()
        r = numpy.random.uniform(0, 1)
        if r <= probabilitate_crossover:
            c1, c2 = crossover_unipunct(x1, x2, n)
            flag, fitness = ok(c1, n, c, v, cmax)
            if flag == True:
                c1 = list(c1)
                c1 = c1 + [fitness]
                copii[i] = c1.copy()
            flag, fitness = ok(c2, n, c, v, cmax)
            if flag == True:
                c2 = list(c2)
                c2 = c2 + [fitness]
                copii[i + 1] = c2.copy()
    return copii
#nu am conditii => sterg tot ce e cu flag

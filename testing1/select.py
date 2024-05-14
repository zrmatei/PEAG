def fps(fitnessuri, dim):
    fps = numpy.zeros(dim)
    suma = numpy.sum(fitnessuri)
    for i in range(dim):
        fps[i] = fitnessuri[i] / suma
    qfps = fps.copy()
    for i in range(1, dim):
        qfps[i] = qfps[i - 1] + fps[i]
    return qfps  # return array()


def ruleta(pop_initiala, dim, n):
    pop_initiala = numpy.asarray(pop_initiala)
    parinti = pop_initiala.copy()
    fitnessuri = numpy.zeros(dim, dtype="float")
    for i in range(dim):
        fitnessuri[i] = pop_initiala[i][n]
    qfps = fps(fitnessuri, dim)
    for i in range(dim):
        r = numpy.random.uniform(0, 1)
        pozitie = numpy.where(qfps >= r)
        index_buzunar_ruleta = pozitie[0][0]
        parinti[i][0:n] = pop_initiala[index_buzunar_ruleta][0:n]
        parinti[i][n] = fitnessuri[index_buzunar_ruleta]
    return parinti


def SUS(pop_initiala, dim, n):
    pop_initiala = numpy.asarray(pop_initiala)
    parinti = pop_initiala.copy()  # gene si fitness-uri
    fitnessuri = numpy.zeros(dim, dtype="float")
    for i in range(dim):
        fitnessuri[i] = pop_initiala[i][n]
    qfps = fps(fitnessuri, dim)
    r = numpy.random.uniform(0, 1 / dim)
    k, i = 0, 0
    while k < dim:
        while r <= qfps[i]:
            parinti[k][0:n] = pop_initiala[i][0:n]
            parinti[k][n] = fitnessuri[i]
            r = r + 1 / dim
            k = k + 1
        i = i + 1
    return parinti

def SelectieParinti():
    pop_initiala, dim, n, c = gen(10)
    parinti = ruleta(pop_initiala, dim, n)
    pop_initiala = numpy.asarray(pop_initiala)
    parinti = numpy.asarray(parinti)
    return pop_initiala, parinti


def turneu(pop_initiala, dim, n, k): #k - dim indivzi alesi aleator / dim turneu
    parinti = pop_initiala.copy()
    fitnessuri = numpy.zeros(dim)
    for i in range(dim):
        fitnessuri[i] = pop_initiala[i][n]
    for i in range(dim):
        submultimePozitiiIndivizi = numpy.random.randint(0, dim, k)
        fitnessuriIndiviziSelectati = [fitnessuri[submultimePozitiiIndivizi[i]] for i in range(k)]
        fitnessIndividCastigator = max(fitnessuriIndiviziSelectati)
        pozMax = numpy.where(fitnessuriIndiviziSelectati == fitnessIndividCastigator)
        indexPozMax = pozMax[0][0]
        # index = corespondentul lui indexPozMax in pop_initiala
        index = submultimePozitiiIndivizi[indexPozMax]
        parinti[i][0:n] = pop_initiala[index][0:n]
        parinti[i][n] = fitnessuri[index]
    return parinti

#alt tip de turneu (nu stiu daca e ok asta)
def turnir(pop, dim, n, k):
    parinti = pop.copy()
    fitnessuri = [individ[-1] for individ in pop]
    for i in range(dim):
        participanti = np.random.choice(dim, k, replace=False)
        index_castigator = np.argmax([fitnessuri[j] for j in participanti])
        parinte_castigator = pop[participanti[index_castigator]].copy()
        parinti[i] = parinte_castigator
    return parinti

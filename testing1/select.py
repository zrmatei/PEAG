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
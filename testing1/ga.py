# evolutia - cat timp
    #                - nu am depasit NMAX  si
    #                - populatia are macar 2 indivizi cu calitati diferite  si
    #                - in ultimele NMAX/4 iteratii s-a schimbat macar o data calitatea cea mai buna

def GA(cost_max, dim, NMAX, pc, pm):
    pop_initiala, dim, n, c, v, cost_max = gen(cost_max, dim)
    pop_initiala = numpy.asarray(pop_initiala)
    istoric_bun = [numpy.max(pop_initiala[:, -1])]

    gen_parcurse = 0  # contor pentru numarul de iteratii (generatii) parcurse
    gata = False  # pt oprire algoritmului daca ating conditiile de oprire
    nrm = 1  # contor pentru numarul maxim de iteratii consecutive fara imbunatatirea celui mai bun individ

    while gen_parcurse < NMAX and not gata:
        parinti = ruleta(pop_initiala, dim, n)
        pop_copii = crossover_populatie(parinti, dim, n, c, v, cost_max, pc)
        pop_copii_mutanti = mutatie_populatie(pop_copii, dim, n, c, v, cost_max, pm)
        pop_urmatoare = elitism(pop_initiala, pop_copii_mutanti, dim, n)
        minim = numpy.min(pop_urmatoare[:, -1])
        maxim = numpy.max(pop_urmatoare[:, -1])

        if maxim == istoric_bun[gen_parcurse]: # daca cel mai bun individ de acum e egal cu ultimul adaugat in lista cu cei mai buni
            nrm = nrm + 1
        else:
            nrm = 0  # la orice imbunatatire resetez contorul la zero

        if maxim == minim or nrm == int(NMAX / 4): # daca max=min (adica toti indivizii sunt identici calitativ) sau daca in ultimele nmax/4 iteratii consecutive nu s-a imbunatatit calitatea
            gata = True  # stop
        else:
            gen_parcurse = gen_parcurse + 1  #inc contor generatii
        istoric_bun.append(numpy.max(pop_urmatoare[:, -1]))   #salvez cel mai bun individ in istoric

        pop_initiala = pop_urmatoare.copy() #init pop initiala de la pas urmator cu pop urmatoare de la gen curenta

    # FINISH ALGORITM de aici; transform din lista in vector pentru a aplica functia where corect
    poz_max = numpy.where(pop_urmatoare[:, -1] == maxim)
    print(poz_max)
    individ_max_gene = pop_urmatoare[poz_max[0][0], 0:n]
    individ_max_fitness = maxim
    return individ_max_gene, individ_max_fitness